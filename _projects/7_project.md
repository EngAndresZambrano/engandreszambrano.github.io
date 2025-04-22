---
layout: page
title: DNS Script with AI DNS Auditing via Prompt Engineering and Shodan API
description: A Python-based DNS auditing tool developed using prompt engineering with ChatGPT and the Shodan API. Designed for academic purposes, it runs in a secure virtual environment and demonstrates the use of AI in cybersecurity automation.
img: assets/img/img_title7.jpg
importance: 7
category: 2025 academic
images:
  lightbox2: true
---

<h3>🧠 DNS Audit Tool — Highlights of Development</h3>
<p>This project showcases the development of a Python-based application designed to perform DNS audits in two modes: basic and advanced. The script leverages the Shodan API to retrieve information about publicly exposed devices and services. Its implementation was guided through prompt engineering techniques using ChatGPT, allowing for the iterative and structured development of functionalities based on carefully crafted prompts. The GUI was built using <code>tkinter</code>.</p>

<p><strong>Note:</strong> This academic project was developed in a controlled, secure virtual environment (internal network, VM with Kali Linux, firewall, VPN) to avoid any potential network risks.</p>

<h3>⚙️ Project Objective</h3>
<ul>
  <li>Design a Python application with a GUI that leverages the Shodan API to identify publicly exposed DNS servers.</li>
  <li><strong>Basic Mode:</strong> Simple detection of exposed DNS IPs.</li>
  <li><strong>Advanced Mode:</strong> Recursive check, secure DNS verification, software fingerprinting, and pagination support.</li>
</ul>

<h3>🧩 Prompt Engineering Strategy</h3>
<p>Prompt engineering was a critical component in designing the application with ChatGPT. The methodology included:</p>
<ul>
  <li>Defining specific roles for the AI (e.g., cybersecurity engineer)</li>
  <li>Providing detailed, layered requests (basic → advanced)</li>
  <li>Requesting secure code practices and updated libraries</li>
  <li>Asking for references and justifications</li>
  <li>Iterative debugging through feedback-based prompts</li>
</ul>

<h3>🖼️ Prerequisites & Initial Prompts Response</h3>
<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <!-- Insert image showing Shodan API prompt setup -->
    <img src="/assets/img/shodan_setup.png" alt="Shodan API Prompt" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    <p class="caption mt-2 text-center">Services identified via Shodan setup prompt.</p>
  </div>
</div>
<p>Initial prompts focused on:</p>
<ul>
  <li>Defining the structure of the GUI</li>
  <li>Integrating the Shodan API for IP discovery</li>
  <li>Verifying server responsiveness</li>
</ul>

<h3>📝 Key Highlight: Prerequisites and Package Installation</h3>
<pre><code class="language-bash">pip install shodan geopy dnspython</code></pre>

<h3>💻 Code Snippet: Basic DNS Scan GUI 🧪</h3>
<pre><code class="language-python">import tkinter as tk
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

    boton_iniciar = tk.Button(
        ventana,
        text="Iniciar Escaneo",
        command=lambda: iniciar_busqueda(entrada_api.get(), texto_salida)
    )
    boton_iniciar.pack(pady=5)

    ventana.mainloop()
</code></pre>
<p>📌 This snippet demonstrates the basic <code>tkinter</code> structure used to dynamically display scan results.</p>

<h3>📉 Troubleshooting & Refinement</h3>
<ul>
  <li>Initial results were blocked by protected DNS servers</li>
  <li>Prompt modified to print debug messages and improve error visibility</li>
  <li>Log messages added directly in the GUI for transparency</li>
</ul>

<h3>🧠 Advanced Functionality: Prompt 3</h3>
<ul>
  <li>Recursive DNS verification</li>
  <li>Pagination of Shodan search results</li>
  <li>Secure DNS provider detection (Cloudflare, Google DNS, Quad9)</li>
  <li>Fingerprinting DNS server software via Shodan metadata</li>
</ul>

<h3>💡 Code Insight: DNS Recursion Check</h3>
<pre><code class="language-python">def is_recursive_dns(ip):
    try:
        query = dns.message.make_query("example.com", dns.rdatatype.A)
        response = dns.query.udp(query, ip, timeout=2)
        return response.flags & dns.flags.RA != 0
    except Exception:
        return False</code></pre>

<h3>📦 Export Results to CSV</h3>
<p>Results are saved for further analysis. Recursive and secure servers are prioritized.</p>
<p><strong>File:</strong> <code>dns_scan_results.csv</code><br/><strong>Location:</strong> Root directory of the script</p>

<h3>🧾 Example Output</h3>
<pre><code class="language-csv">IP,Country,Coordinates,Recursive,Secure
8.8.8.8,USA,"37.751, -97.822",Yes,Yes
185.228.xxx.x,Israel,"xx.0853, xx.7818",Yes,Yes</code></pre>

<h4>🔽 Download Advanced Mode Script :</h4>
 <div class="mt-4">
    <a href="{{ '/assets/pdf/scandnsadvcsv.py' | relative_url }}" class="btn btn-primary" download>
      🐍 Download Python Script
    </a>
  </div>

<h3>📸 Visual Output</h3>

<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/gui_start.png" data-lightbox="standards" data-title="Initial Prompt Window">
      <img src="/assets/img/gui_start.png" alt="Initial Prompt Window" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Script Window Initialization.
    </div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/scan_feedback.png" data-lightbox="standards" data-title="Scanning Results">
      <img src="/assets/img/scan_feedback.png" alt="Scanning Results" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Execution Feedback.
    </div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/csv_validation.png" data-lightbox="standards" data-title="CSV File Results">
      <img src="/assets/img/csv_validation.png" alt="CSV File Results" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Final CSV File Validation.
    </div>
  </div>
</div>

<h3>📚 References</h3>
<ul>
  <li>OpenAI. (2025). ChatGPT (version 4). https://chatgpt.com/</li>
  <li>Shodan API Docs. https://developer.shodan.io/</li>
  <li>dnspython Docs. https://dnspython.readthedocs.io/</li>
  <li>Geopy Docs. https://geopy.readthedocs.io/</li>
  <li>https://www.xataka.com/basics/como-mejorar-respuestas-chatgpt-9-pasos-para-garantizar-mayor-calidad-mejores-fuentes</li>
  <li>https://skimai.com/es/las-personas-en-la-ingenieria-rapida/</li>
  <li>https://docs.python.org/3/library/tkinter.html</li>
  <li>https://www.vpnbook.com/freevpn</li>
  <li>https://protonvpn.com/</li>
  <li>https://whatismyipaddress.com/</li>
</ul>

<h3>🧠 Conclusions</h3>
<ul>
  <li>AI-powered prompt engineering accelerated structured code generation</li>
  <li>GUI application effectively identified public DNS exposures</li>
  <li>Audit time significantly reduced through automation</li>
  <li>Prompt iteration ensured resilience against network limitations</li>
</ul>


