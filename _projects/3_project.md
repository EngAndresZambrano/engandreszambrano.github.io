---
layout: page
title: Black Box Audit Report - Vulnerability Assessment with Metasploit, Nessus, and PwnDoc
description: A professional black box audit conducted on a virtual machine using tools like Metasploit, Nmap, and Nessus. The final report was structured with PwnDoc and includes technical findings, CVE exploitation, and step-by-step documentation.
img: assets/img/img_title3.jpg
importance: 3
category: academic
---

This project presents a complete black box vulnerability assessment conducted on a virtual machine, simulating a real-world offensive security audit. The audit was performed using Kali Linux and a range of industry-standard tools, including Metasploit, Nmap, Gobuster, Nessus, and others.

The findings were compiled into a professional audit report using PwnDoc:

  <div class="mt-4">
    <a href="{{ '/assets/pdf/PwDoc_audit_report.pdf' | relative_url }}" class="btn btn-primary" download>
      📄 Download full audit report PDF
    </a>
  </div>
  
Which ensures a structured format with key sections such as execution timeline, executive summary, vulnerability overview, and detailed technical analysis. The report covers several critical and high-severity vulnerabilities, including:

CVE-2023-26048 (Jetty DDoS vulnerability)

CVE-2024-23897 (Arbitrary file read in Jenkins)

CVE-2024-40725 (Source code disclosure)

Privilege escalation via GNU Screen 4.5.0

Weak/default credentials and web-based injection attempts

Each vulnerability is documented with exploitation steps, screenshots, and analysis. The project also includes a step-by-step manual outlining the audit methodology and the use of each tool throughout the process.

  <div class="mt-4">
    <a href="{{ '/assets/pdf/Step-by-Step_manual.pdf' | relative_url }}" class="btn btn-primary" download>
      📄 Download full step-by-step manual PDF
    </a>
  </div>
  
Designed for both educational and professional development purposes, this project demonstrates how to conduct and document a complete security audit following industry standards.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
