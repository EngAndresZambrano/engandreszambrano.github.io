---
layout: page
title:  SSH and Telnet Audit Application Using Shodan API
description: A Python application for auditing SSH and Telnet services, leveraging the Shodan API and prompt engineering with AI. The application scans the network and exports findings in CSV format for further analysis.
img: assets/img/img_title8.png
importance: 8
category: 2025 academic
---

<h3>🧠 DNS Audit Tool — Highlights of Development</h3>
<p>This project involves the development of a Python application designed to perform SSH and Telnet service audits using the Shodan API. The application is created with prompt engineering and AI, focusing on scanning services to identify vulnerabilities. The environment for this audit is a virtual machine with an internal network protected by a firewall to prevent unauthorized traffic, and a VPN service is deployed on the host machine to obscure the IP address. After completing the scan, the application exports the findings into a CSV file, providing a comprehensive report for further review. This audit is carried out in a controlled, academic environment, ensuring security measures are in place to prevent any impact on the virtual environment. The GUI was built using <code>tkinter</code>.</p>

<p><strong>Note:</strong> This academic project was developed in a controlled, secure virtual environment (internal network, VM with Kali Linux, firewall, VPN) to avoid any potential network risks.</p>

<h3>🧩 Prompt Engineering Strategy</h3>
<p>Prompt engineering was a critical component in designing the application with ChatGPT. The methodology included:</p>
<ul>
  <li>Defining specific roles for the AI (e.g., cybersecurity engineer)</li>
  <li>Providing detailed, layered requests (basic → advanced)</li>
  <li>Requesting secure code practices and updated libraries</li>
  <li>Asking for references and justifications</li>
  <li>Iterative debugging through feedback-based prompts</li>

  <h2>🔍 SSH and Telnet Services Audit</h2>

    <p>
      This application was developed in Python with a Tkinter-based graphical interface, compatible with Kali Linux. It audits SSH and Telnet services exposed on the internet by querying the Shodan API. The tool automates access attempts using common credentials to identify vulnerable systems.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
      <div>
        <h3>🛠️ Technologies Used</h3>
        <ul>
          <li>Python 3</li>
          <li>Tkinter (GUI)</li>
          <li>Paramiko (SSH)</li>
          <li>telnetlib3 (Telnet)</li>
          <li>Shodan API</li>
          <li>CSV (results export)</li>
        </ul>
      </div>
      <div>
        <h3>🔐 Security-Focused Approach</h3>
        <ul>
          <li>Auditing within controlled environments</li>
          <li>Internal network protected by VPN and firewall</li>
          <li>Isolated test credentials</li>
          <li>Secure connection practices</li>
          <li>Ethical hacking principles respected</li>
        </ul>
      </div>
    </div>

    <h3>📋 Key Features</h3>
    <ul class="list-decimal list-inside text-gray-600 mb-4">
      <li>Queries exposed IPs via Shodan on ports 22 (SSH) and 23 (Telnet)</li>
      <li>Automatically attempts login using common credentials</li>
      <li>Graphical interface to display connection attempts and results</li>
      <li>Exports successful logins to a CSV file</li>
      <li>Reads credentials from a local file</li>
    </ul>

    <h3 class="text-lg font-semibold text-gray-700 mb-2">📸 Screenshots</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
      <img src="/assets/proyecto2-api.png" alt="API Input Window" class="rounded-lg shadow-lg">
      <img src="/assets/proyecto2-ejecucion.png" alt="Scan in Progress" class="rounded-lg shadow-lg">
      <img src="/assets/proyecto2-resultados.png" alt="Scan Results" class="rounded-lg shadow-lg">
      <img src="/assets/proyecto2-csv.png" alt="Generated CSV File" class="rounded-lg shadow-lg">
    </div>

    <div class="mb-4">
      <h3 class="text-lg font-semibold text-gray-700">🧪 Conclusions</h3>
      <p class="text-gray-600">
        This project highlighted that many servers remain exposed with default or weak credentials. Automated auditing tools such as this one are essential for identifying vulnerabilities and promoting best practices in secure network service management.
      </p>
    </div>

    <div class="text-sm text-gray-500 italic">
      References: <br>
      <a href="https://developer.shodan.io/" class="underline">developer.shodan.io</a> ·
      <a href="https://www.paramiko.org/" class="underline">paramiko.org</a> ·
      <a href="https://pypi.org/project/telnetlib3/" class="underline">telnetlib3</a> ·
      <a href="https://docs.python.org/3/library/tkinter.html" class="underline">tkinter docs</a>
    </div>

    <h4>🔽 Download Scanner Audit Script :</h4>
    <div class="mt-4">
        <a href="{{ '/assets/pdf/scriptSSHTelnet.py' | relative_url }}" class="btn btn-primary" download>
        🐍 Download Python Script
      </a>
    </div>
