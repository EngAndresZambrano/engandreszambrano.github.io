---
layout: page
title: DNS Script with AI DNS Auditing via Prompt Engineering and Shodan API
description: A Python-based DNS auditing tool developed using prompt engineering with ChatGPT and the Shodan API. Designed for academic purposes, it runs in a secure virtual environment and demonstrates the use of AI in cybersecurity automation.
img: assets/img/img_title7.jpg
importance: 7
category: academic
images:
  lightbox2: true
---

This project showcases the development of a Python-based application designed to perform DNS audits in two modes: basic and advanced. The script leverages the Shodan API to retrieve information about publicly exposed devices and services. Its implementation was guided through prompt engineering techniques using ChatGPT, allowing for the iterative and structured development of functionalities based on carefully crafted prompts.

To ensure a secure testing environment, the tool was deployed within a virtual machine configured with an internal network and a firewall, while the host machine was connected through a VPN to mask its IP address. The project incorporates cybersecurity best practices and includes manual verification of the AI-generated outputs to ensure accuracy and minimize potential vulnerabilities.

Developed for academic purposes, this project highlights the potential of large language models in automating cybersecurity tasks, emphasizing how effective prompt engineering can enhance AI-assisted development.

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Explicación del Script de Escaneo DNS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2em;
            line-height: 1.6;
        }
        h3 {
            color: #2c3e50;
            margin-top: 2em;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

<h2>Explicación del Script de Escaneo DNS</h2>

<h3>📌 Descripción General</h3>
<p>
Este script en Python realiza un escaneo de servidores DNS expuestos utilizando la API de <strong>Shodan</strong>. Además de verificar la actividad del servidor DNS, evalúa si es recursivo y si pertenece a una lista de servidores seguros. El resultado puede exportarse en un archivo CSV. También incluye una interfaz gráfica con <code>tkinter</code>.
</p>

<h3>🔧 Librerías Utilizadas</h3>
<ul>
    <li><code>tkinter</code>: Para crear la interfaz gráfica.</li>
    <li><code>shodan</code>: Acceso a la base de datos de Shodan.</li>
    <li><code>socket</code>: No se usa directamente, pero está importado.</li>
    <li><code>geopy</code>: Para obtener ubicaciones a partir de coordenadas.</li>
    <li><code>threading</code>: Para ejecutar el escaneo sin bloquear la interfaz.</li>
    <li><code>dns.query</code> y <code>dns.message</code>: Para hacer consultas DNS.</li>
    <li><code>csv</code>: Para exportar resultados a un archivo.</li>
</ul>

<h3>🛡️ DNS Seguros</h3>
<p>
Se define una lista con direcciones IP de servidores DNS conocidos por ser seguros:
<code>{"Quad9": "9.9.9.9", "Cloudflare": "1.1.1.1", "Google": "8.8.8.8"}</code>
</p>

<h3>📍 Función <code>obtener_ubicacion()</code></h3>
<p>
Utiliza <code>geopy</code> para traducir coordenadas geográficas en una dirección legible.
</p>

<h3>🔎 Funciones <code>verificar_dns()</code> y <code>verificar_recursividad()</code></h3>
<p>
Ambas funciones usan consultas DNS para verificar:
<ul>
    <li>Si el servidor responde (<strong>activo</strong>).</li>
    <li>Si es <strong>recursivo</strong>, es decir, si puede resolver nombres fuera de su zona.</li>
</ul>
</p>

<h3>📄 Función <code>generar_csv()</code></h3>
<p>
Genera un archivo CSV ordenando primero los servidores recursivos y seguros. Guarda columnas como IP, país, ubicación, software detectado, si es recursivo y si es seguro.
</p>

<h3>🚀 Función <code>realizar_busqueda()</code></h3>
<p>
Es el núcleo del escaneo. Usa la API de Shodan para encontrar servidores en el puerto 53 (DNS), y luego ejecuta las verificaciones mencionadas arriba. Muestra los resultados en la interfaz y genera el archivo CSV.
</p>

<h3>🖥️ Interfaz Gráfica</h3>
<p>
Usa <code>tkinter</code> para pedir una clave API y mostrar los resultados. Al hacer clic en el botón <strong>"Iniciar Escaneo"</strong>, se ejecuta el análisis en un hilo aparte para no congelar la GUI.
</p>

<h3>🧵 Multihilo</h3>
<p>
Se usa <code>threading.Thread</code> para que el escaneo se ejecute sin bloquear la interfaz gráfica.
</p>

<h3>📦 Exportación de Resultados</h3>
<p>
Los datos obtenidos se guardan en un archivo <code>dns_scan_results.csv</code>, permitiendo análisis posteriores.
</p>

<h3>🔚 Estructura Principal</h3>
<p>
El script se ejecuta directamente si se corre como archivo principal, llamando a <code>crear_interfaz()</code>.
</p>

</body>
</html>
