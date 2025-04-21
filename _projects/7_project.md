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

<h3>🧠 DNS Audit Tool — Highlights of Development</h3>

<p>This page presents the key elements, stages, and results obtained during the development of a DNS auditing tool using Python and Shodan's API. The purpose of the application is to facilitate DNS service auditing in two distinct modes: <strong>Basic</strong> and <strong>Advanced</strong>, offering a visual interface for Windows through <code>tkinter</code>.</p>

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
  <li>✅ Defining specific roles for the AI (e.g., cybersecurity engineer)</li>
  <li>✅ Providing detailed, layered requests (basic → advanced)</li>
  <li>✅ Requesting secure code practices and updated libraries</li>
  <li>✅ Asking for references and justifications</li>
  <li>✅ Iterative debugging through feedback-based prompts</li>
</ul>

<h3>🖼️ Prerequisites & Initial Prompts</h3>
<div class="image-box">
  <!-- 📷 Insert Image 1: Shodan API setup or initial prompt request -->
  <img src="assets/img/shodan_setup.jpg" alt="Shodan API Prompt" />
</div>
<p>Initial prompts focused on:</p>
<ul>
  <li>Defining the structure of the GUI</li>
  <li>Integrating the Shodan API for IP discovery</li>
  <li>Verifying server responsiveness</li>
</ul>

<h3>📝 Key Highlight: Prerequisites and Package Installation</h3>

```bash
pip install shodan geopy dnspython
<h3>💻 Code Snippet: Basic DNS Scan GUI 🧪</h3>
python
Copiar
Editar
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("DNS Scan")
label = tk.Label(root, text="Scanning...", font=("Arial", 14))
label.pack(pady=20)

# More code to interface with Shodan and scan IPs...
root.mainloop()
<p>📌 This snippet shows the basic <code>tkinter</code> structure to display scan results dynamically.</p> <h3>📉 Troubleshooting & Refinement</h3> <p>Initial implementation did not return visible results due to network protection on DNS servers.</p> <ul> <li>✅ Adjusted prompt to include debug feedback and error printouts</li> <li>✅ Log visibility was added to the GUI to improve transparency</li> </ul> <h3>🧠 Advanced Functionality: Prompt 3</h3> <p>Four advanced functions were integrated:</p> <ul> <li>Recursive DNS checks</li> <li>Pagination of Shodan results</li> <li>Secure DNS match (Cloudflare, Google DNS, Quad9)</li> <li>Server software identification via Shodan metadata</li> </ul> <h3>💡 Code Insight: DNS Recursion Check</h3>
python
Copiar
Editar
def is_recursive_dns(ip):
    try:
        query = dns.message.make_query("example.com", dns.rdatatype.A)
        response = dns.query.udp(query, ip, timeout=2)
        return response.flags & dns.flags.RA != 0
    except Exception:
        return False
<h3>📦 Export Results to CSV</h3> <p>To enhance post-analysis, a final prompt enabled CSV export. IPs that are recursive and secure are prioritized in the output.</p> <p><strong>🗂️ File Name:</strong> <code>dns_scan_results.csv</code><br/> <strong>📍 Location:</strong> Same directory as the script</p> <h3>🧾 Example Output</h3>
csv
Copiar
Editar
IP,Country,Coordinates,Recursive,Secure
8.8.8.8,USA,"37.751, -97.822",Yes,Yes
185.228.168.9,Israel,"32.0853, 34.7818",Yes,Yes
...
<h4>🔽 Download Full Report:</h4>
html
Copiar
Editar
<a href="dns_scan_results.csv" download>
  <button>📥 Download Full Scan Report</button>
</a>
<h3>📸 Visual Output</h3> <ul> <li><strong>Image 1 - Script Window Initialization</strong><br/> <!-- 📷 Add screenshot showing "Enter Shodan API" prompt --> <img src="assets/img/gui_start.jpg" alt="Initial Prompt Window" /></li> <li><strong>Image 2 - Execution Feedback</strong><br/> <!-- 📷 Add image of scanning process in the GUI window --> <img src="assets/img/scan_feedback.jpg" alt="Scanning Results" /></li> <li><strong>Image 3 - Final CSV File Validation</strong><br/> <!-- 📷 Screenshot from Notepad++ showing CSV results --> <img src="assets/img/csv_validation.jpg" alt="CSV File Results" /></li> </ul> <h3>🧾 References</h3> <ul> <li>OpenAI. (2025). ChatGPT (version 4) [Large Language Model]. https://chatgpt.com/</li> <li>Shodan API Docs. https://developer.shodan.io/</li> <li>dnspython Documentation. https://dnspython.readthedocs.io/</li> <li>Geopy Documentation. https://geopy.readthedocs.io/</li> </ul> <h3>🧠 Conclusions</h3> <ul> <li>The AI-assisted development process allowed for effective modular design and debugging.</li> <li>The tool successfully identified exposed DNS servers in real-time.</li> <li>It significantly reduced manual audit time from hours to minutes.</li> <li>Despite network protection limitations, intelligent prompt refinements ensured continuous improvement.</li> </ul> ```

<h3>📌 General Overview</h3>
<p>
This Python script audits exposed DNS servers by leveraging the <strong>Shodan API</strong>. It checks whether a DNS server is active, recursive, and if it belongs to a known safe provider. Results are optionally exported to a CSV file. The tool includes a GUI built with <code>tkinter</code>.
</p>

<h3>🔧 Used Libraries</h3>
<ul>
    <li><code>tkinter</code>: Builds the graphical interface.</li>
    <li><code>shodan</code>: Interfaces with the Shodan API.</li>
    <li><code>socket</code>: (Imported, but unused in this script.)</li>
    <li><code>geopy</code>: Converts coordinates into human-readable addresses.</li>
    <li><code>threading</code>: Enables non-blocking operations via background threads.</li>
    <li><code>dns.query</code> and <code>dns.message</code>: Used for DNS queries and checks.</li>
    <li><code>csv</code>: Outputs audit data into structured CSV format.</li>
</ul>

<h3>🛡️ Trusted DNS Providers</h3>
<p>
The script compares scanned IPs against a predefined list of well-known secure DNS providers:
<code>{"Quad9": "9.9.9.9", "Cloudflare": "1.1.1.1", "Google": "8.8.8.8"}</code>
</p>

<h3>📍 Function <code>obtener_ubicacion()</code></h3>
<p>
Uses <code>geopy</code> to resolve latitude and longitude into a human-readable address. Returns “Unknown” if the location cannot be determined.
</p>

<h3>🔎 Functions <code>verificar_dns()</code> and <code>verificar_recursividad()</code></h3>
<p>
These functions check whether:
<ul>
    <li>The DNS server is active (responds to queries).</li>
    <li>It is recursive (resolves names beyond its authoritative domain).</li>
</ul>
</p>

<h3>📄 Function <code>generar_csv()</code></h3>
<p>
Sorts the collected data by recursion and trustworthiness, then writes it to <code>dns_scan_results.csv</code> with fields such as IP address, country, software, and more.
</p>

<h3>🚀 Function <code>realizar_busqueda()</code></h3>
<p>
The core logic. This function sends a query to Shodan to find devices with port 53 open. It verifies each result, determines location, software, and security status, and optionally writes them into a CSV file.
</p>

<h3>🖥️ Graphical Interface</h3>
<p>
Built with <code>tkinter</code>, the interface includes a field for the Shodan API key, a results window, and a button to launch the scan. The scan runs in a separate thread to keep the interface responsive.
</p>

<h3>🧵 Multithreading</h3>
<p>
Uses <code>Thread</code> from Python’s <code>threading</code> module to avoid freezing the interface during potentially long-running scans.
</p>

<h3>📦 Output and Reports</h3>
<p>
Collected data is saved to a CSV file for further analysis and documentation.
</p>

<h3>🔚 Entry Point</h3>
<p>
If the script is run directly (not imported as a module), it launches the GUI by calling <code>crear_interfaz()</code>.
</p>

