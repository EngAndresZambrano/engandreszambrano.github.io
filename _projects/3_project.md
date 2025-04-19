---
layout: page
title: Black Box Audit Report - Vulnerability Assessment with Metasploit, Nessus, and PwnDoc
description: A professional black box audit conducted on a virtual machine using tools like Metasploit, Nmap, and Nessus. The final report was structured with PwnDoc and includes technical findings, CVE exploitation, and step-by-step documentation.
img: assets/img/img_title3.jpg
importance: 3
category: academic
images:
  lightbox2: true
---

This project presents a complete black box vulnerability assessment conducted on a virtual machine, simulating a real-world offensive security audit. The audit was performed using Kali Linux and a range of industry-standard tools, including Metasploit, Nmap, Gobuster, Nessus, and others.

The findings were compiled into a professional audit report using PwnDoc:

  <div class="mt-4">
    <a href="{{ '/assets/pdf/PwDoc_audit_report.pdf' | relative_url }}" class="btn btn-primary" download>
      📄 Download full audit report PDF
    </a>
  </div>
  
Which ensures a structured format with key sections such as execution timeline, executive summary, vulnerability overview, and detailed technical analysis. 

<div class="row mt-4">
   <div class="col-sm mt-3 mt-md-0 text-center">
      <a href="/assets/img/portada.png" data-lightbox="grupo1" data-title="Black Box Services">
      <img src="/assets/img/portada.png" alt="Black Box Services" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
   </a>
</div>
<div class="caption">
    Services identified on the black box after conducting the ethical hacking activity.
</div>

The report covers several critical and high-severity vulnerabilities, including:

 <strong>CVE-2023-26048 (Jetty DDoS vulnerability)</strong>

 <strong>CVE-2024-23897 (Arbitrary file read in Jenkins)</strong>

 <strong>CVE-2024-40725 (Source code disclosure)</strong>

 <strong>Privilege escalation via GNU Screen 4.5.0</strong>

 <strong>Weak/default credentials and web-based injection attempts</strong>

 <div class="row text-center mt-4">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/owasp.png" data-lightbox="standards1" data-title="OWASP">
      <img src="/assets/img/owasp.png" alt="OWASP" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/nessus.png" data-lightbox="standards1" data-title="Nessus">
      <img src="/assets/img/nessus.png" alt="Nessus" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/nikto.png" data-lightbox="standards1" data-title="Nikto">
      <img src="/assets/img/nikto.png" alt="Nikto" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">
    Tools employed for port and service scanning during the assessment.
</div>

Each vulnerability is documented with exploitation steps, screenshots, and analysis. The project also includes a step-by-step manual outlining the audit methodology and the use of each tool throughout the process.

  <div class="mt-4">
    <a href="{{ '/assets/pdf/Step-by-Step_manual.pdf' | relative_url }}" class="btn btn-primary" download>
      📄 Download full step-by-step manual PDF
    </a>
  </div>
  
Designed for both educational and professional development purposes, this project demonstrates how to conduct and document a complete security audit following industry standards.

<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/matasploit.png" data-lightbox="standards2" data-title="Metasploit">
      <img src="/assets/img/metasploit.png" alt="Metasploit" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/gobuster.png" data-lightbox="standards2" data-title="Gobuster">
      <img src="/assets/img/gobuster.png" alt="Gobuster" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption">
   Root directory file enumeration using Gobuster and vulnerability exploitation with Metasploit.
</div>

The following images display the key findings from the activity. Using the John the Ripper tool, a hash found in the passwd file was successfully cracked for the user 'kali'. With these credentials, privilege escalation was achieved through the execution of a setuid binary, utilizing Radare2 for analysis and exploitation.

<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/ripper.png" data-lightbox="standards3" data-title="Cracked Password">
      <img src="/assets/img/ripper.png" alt="Cracked Password" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/privilegios.png" data-lightbox="standards3" data-title="Privilege Escalation">
      <img src="/assets/img/privilegios.png" alt="Privilege Escalation" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

