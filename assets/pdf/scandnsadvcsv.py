import tkinter as tk
from tkinter import scrolledtext, messagebox
import shodan
import socket
from geopy.geocoders import Nominatim
from threading import Thread
import dns.query
import dns.message
import csv

# Lista de DNS seguros para comparación
DNS_SEGUROS = {"Quad9": "9.9.9.9", "Cloudflare": "1.1.1.1", "Google": "8.8.8.8"}

def log_message(texto_salida, mensaje):
    texto_salida.insert(tk.END, mensaje + "\n")
    texto_salida.see(tk.END)
    texto_salida.update()

def obtener_ubicacion(lat, lon):
    try:
        geolocator = Nominatim(user_agent="GeopyUserName")
        location = geolocator.reverse(f"{lat}, {lon}", language='es')
        return location.address if location else "Ubicación desconocida"
    except Exception as e:
        return f"Error obteniendo ubicación: {str(e)}"

def verificar_dns(ip):
    try:
        query = dns.message.make_query("www.example.com", dns.rdatatype.A)
        response = dns.query.udp(query, ip, timeout=2)
        return bool(response and response.answer)
    except Exception:
        return False

def verificar_recursividad(ip):
    try:
        query = dns.message.make_query("www.example.com", dns.rdatatype.A, want_dnssec=True)
        response = dns.query.udp(query, ip, timeout=2)
        return bool(response.flags & dns.flags.RA)
    except Exception:
        return False

def generar_csv(resultados):
    try:
        resultados.sort(key=lambda x: (not x['Recursivo'], not x['Seguro']))
        with open("dns_scan_results.csv", "w", newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["IP", "País", "Ubicación", "Software", "Recursivo", "Seguro"])
            escritor.writeheader()
            escritor.writerows(resultados)
        return "dns_scan_results.csv"
    except Exception as e:
        return f"Error generando CSV: {str(e)}"

def realizar_busqueda(api_key, texto_salida):
    log_message(texto_salida, "[+] Iniciando escaneo en Shodan...")
    try:
        api = shodan.Shodan(api_key)
        query = 'port:53'
        resultados = api.search(query, page=1)
        log_message(texto_salida, f"[+] {len(resultados['matches'])} servidores encontrados.")
        dns_resultados = []
        
        for servicio in resultados['matches']:
            ip = servicio['ip_str']
            pais = servicio.get('location', {}).get('country_name', 'Desconocido')
            lat = servicio.get('location', {}).get('latitude', None)
            lon = servicio.get('location', {}).get('longitude', None)
            software = servicio.get('product', 'Desconocido')
            
            log_message(texto_salida, f"[-] Verificando IP: {ip} ...")
            dns_activo = verificar_dns(ip)
            recursivo = verificar_recursividad(ip)
            seguro = any(ip == dns_ip for dns_ip in DNS_SEGUROS.values())
            
            if dns_activo:
                ubicacion = obtener_ubicacion(lat, lon) if lat and lon else "Coordenadas no disponibles"
                dns_info = {"IP": ip, "País": pais, "Ubicación": ubicacion, "Software": software, "Recursivo": recursivo, "Seguro": seguro}
                dns_resultados.append(dns_info)
                log_message(texto_salida, f"[✓] DNS activo: {ip}\nPaís: {pais}\nUbicación: {ubicacion}\nSoftware: {software}\nRecursivo: {'Sí' if recursivo else 'No'}\nSeguro: {'Sí' if seguro else 'No'}\n")
            else:
                log_message(texto_salida, f"[✗] Sin respuesta: {ip}")
        
        archivo_csv = generar_csv(dns_resultados)
        log_message(texto_salida, f"[+] Archivo CSV generado: {archivo_csv}")
    except shodan.APIError as e:
        log_message(texto_salida, f"[!] Error de Shodan: {str(e)}")
        messagebox.showerror("Error de Shodan", str(e))
    except Exception as e:
        log_message(texto_salida, f"[!] Error inesperado: {str(e)}")
        messagebox.showerror("Error", str(e))

def iniciar_busqueda(api_key, texto_salida):
    if not api_key:
        messagebox.showwarning("Advertencia", "Por favor ingresa una clave API de Shodan.")
        return
    texto_salida.delete('1.0', tk.END)
    hilo = Thread(target=realizar_busqueda, args=(api_key, texto_salida))
    hilo.start()

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Escaneo DNS")
    ventana.geometry("600x500")

    etiqueta_api = tk.Label(ventana, text="Clave API de Shodan:")
    etiqueta_api.pack(pady=5)

    entrada_api = tk.Entry(ventana, width=50, show='*')
    entrada_api.pack(pady=5)

    texto_salida = scrolledtext.ScrolledText(ventana, width=70, height=25)
    texto_salida.pack(pady=10)

    boton_iniciar = tk.Button(ventana, text="Iniciar Escaneo", command=lambda: iniciar_busqueda(entrada_api.get(), texto_salida))
    boton_iniciar.pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()
