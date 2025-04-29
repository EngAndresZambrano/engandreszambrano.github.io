---
layout: page
title: IDS/IPS Implementation Using PfSense and Suricata
description: This project outlines the installation, configuration, and testing of an IDS/IPS/NSM solution using PfSense for perimeter security and Suricata for intrusion detection, prevention, and network security monitoring.
img: assets/img/img_title6.png
importance: 5
category: 2025 academic
images:
  lightbox2: true
---

# 🛡️ IDS/IPS Implementation Using PfSense and Suricata

This project demonstrates the complete deployment of a perimeter security solution using **PfSense** as a firewall and **Suricata** as an IDS/IPS/NSM system. It includes all necessary configurations, environment preparation, and validation through real-world testing.

## 📌 Introduction

This guide details a practical implementation of network security monitoring, focused on:

- Deploying a virtualized firewall and IDS/IPS system
- Configuring secure and segmented interfaces
- Enabling real-time traffic analysis
- Testing responses to threats and attack simulations

## 🖥️ Environment Prerequisites and Network Diagram

The project was developed in a virtualized environment including:

- **PfSense firewall**
- **Suricata IDS/IPS**
- **Ubuntu DMZ host**
- **Windows test client**
- Auxiliary tools like Snort, MaxMind, and WatchDog

💡 Sugerencia

## ⚙️ Installation and Configuration

### 🔧 PfSense Installation

The first step involves deploying **PfSense** in a virtual machine environment.

- Mount the ISO image in a virtual machine and proceed with the installation process.
- Complete the initial configuration wizard to assign interfaces and set up admin credentials.
- Define the **LAN**, **WAN**, and **DMZ** interfaces according to the desired network topology.
- Assign static IP addresses to ensure consistent routing.

💡 *[SUGERENCIA: Puedes incluir aquí una captura de pantalla del asistente de instalación de PfSense]*

```html
<a href="/assets/img/pfsense_install.png" data-lightbox="install" data-title="PfSense Installation Wizard">
  <img src="/assets/img/pfsense_install.png" alt="PfSense Wizard" class="img-fluid rounded z-depth-1" />
</a>

## 🛡️ Suricata Installation

Once **PfSense** is operational, proceed with installing **Suricata** as the IDS/IPS engine.

- Navigate to the **Package Manager** in the PfSense web interface.
- Install **Suricata** directly from available packages.
- Enable **IDS/IPS mode** to allow inline packet inspection and real-time blocking.
- Select rule sources such as **Emerging Threats Open** and update them to ensure up-to-date threat detection.

💡 *[SUGERENCIA: Puedes agregar aquí una captura del paquete de instalación de Suricata en PfSense]*

```html
<a href="/assets/img/suricata_install.png" data-lightbox="suricata" data-title="Installing Suricata in PfSense">
  <img src="/assets/img/suricata_install.png" alt="Suricata Installation" class="img-fluid rounded z-depth-1" />
</a>

## 🧠 Snort and MaxMind Integration

To improve threat detection and context awareness:

- Import **Snort rule sets** for additional signature-based analysis.
- Integrate **MaxMind GeoIP** databases to classify and act based on traffic origin.

These tools help **Suricata** correlate suspicious activity with known threats and geographic locations, enhancing situational awareness.

---

## 🐶 WatchDog Installation

For system resilience:

- Install **WatchDog** via the PfSense package manager.
- Configure WatchDog to monitor the **Suricata service**.
- Set triggers to **automatically restart Suricata** in case of failure.

This ensures continuous IDS/IPS protection with minimal manual intervention.

---

## 🔐 Firewall Configuration

### 🌐 Interface Configuration

Establish three main zones:

- **LAN** – for internal users
- **WAN** – for internet access
- **DMZ** – for semi-public servers

Manually assign **static IPs** to interfaces to prevent conflicts and maintain routing clarity.

💡 *[SUGERENCIA: Puedes insertar un diagrama aquí con la asignación de interfaces]*

---

### 🔒 Firewall Setup Wizard

Use PfSense’s **Firewall Wizard** to:

- Block **private and reserved networks** on the WAN interface.
- Apply initial **NAT** and **DNS** rules.
- Establish a baseline **deny-all approach** with exceptions as needed.

---

### ✍️ Custom Firewall Rules

Fine-tune traffic filtering with custom rules:

- Permit or deny traffic based on **IP address**, **port**, and **protocol**.
- Enforce **DMZ segmentation** to prevent lateral movement into the LAN.
- Allow essential services like **ICMP**, **SSH**, and **HTTP** for specific tests.

---

## 🧪 Host Configuration and Security

### 🧱 Ubuntu Machine in DMZ

Deploy a **hardened Ubuntu server** in the DMZ:

- **Outbound access** is strictly limited.
- Serves as a **honeypot** or vulnerable server for testing attack scenarios.

💡 *[SUGERENCIA: Puedes mostrar aquí la terminal de Ubuntu mostrando interfaces o logs]*

```html
<a href="/assets/img/ubuntu_dmz.png" data-lightbox="dmz" data-title="Ubuntu DMZ Network Setup">
  <img src="/assets/img/ubuntu_dmz.png" alt="Ubuntu DMZ" class="img-fluid rounded z-depth-1" />
</a>

## 🧠 Suricata Advanced Configuration

### 🗂️ Enabling FireHOL IP Lists

Enhance blocking with **FireHOL IP Lists**:

- Import known **malicious IPs**.
- Use them as a first layer of **automated blocking** in Suricata.

---

### 🔌 Interface Assignment in Suricata

Define monitored interfaces:

- Assign **LAN**, **WAN**, and **DMZ** to Suricata.
- Choose **IDS** (monitoring only) or **IPS** (active blocking) per interface.

---

## 🐾 WatchDog Configuration

- Define **triggers** for Suricata service crashes.
- Optionally enable **email alerts** for administrative notification.
- Ensure Suricata **automatically restarts** to maintain protection.

---

## 🧪 Testing Phase

### 🔥 Firewall Tests

Use tools like **Nmap** to validate:

- **Packet filtering** and access control.
- **Port-level restrictions** and proper system response behavior.

---

### 🧪 Ubuntu DMZ Tests

From the Ubuntu DMZ machine:

- Generate both **legitimate** and **malicious** traffic.
- Validate **egress control** and **Suricata detections**.

---

### 👁️ Suricata IDS/IPS Tests

Simulate common attack techniques:

- **Ping floods**
- **Port scans**
- **Web exploitation attempts**

Observe:

- **Real-time alerts**
- **Blocking actions**
- **Log entries** in the Suricata dashboard.

---

### 🚨 Initial Alert Testing

- Trigger diverse traffic scenarios to **generate alerts**.
- **Tune detection rules** to reduce false positives.
- Review **alert statistics** and refine configurations accordingly.

---

### 🧪 Windows Machine Attack Simulation

Using a **Windows-based host**:

- Launch tools like **Metasploit**, **Netcat**, or **Nmap**.
- Evaluate Suricata’s ability to **detect**, **log**, and **block** these intrusions.

---

### 🔓 Host IP Unblocking

- Review Suricata's **blocked IP list** via the GUI or command line.
- **Manually unblock** false positives.
- Optionally automate IP unblocking using custom **scripts**.

---

### 🌉 Ubuntu in Bridge Mode (Extra Test)

Deploy an additional **Ubuntu system in bridge mode**:

- Enables **passive traffic monitoring**.
- Compare Suricata’s performance and **detection accuracy** in **inline vs passive mode**.

---

<section>
  <h3>✅ Conclusions</h3>
  <ul>
    <li>
      It is evident that implementing an IDS/IPS system (in our case, Suricata) within an architecture that requires safeguarding data in transit or at rest is essential. However, it must be emphasized that the effectiveness of intrusion detection and prevention is directly proportional to the rigor of its configuration and tuning. A well-parameterized system will significantly enhance protection and threat mitigation.
    </li>
    <li>
      When using free security tools such as Snort or FireHOL IP Lists in an enterprise environment, it is vital to establish a regular update schedule. These lists are stored in public repositories and often require manual updates. Considering that adversaries are constantly evolving and deploying new malicious IP addresses, maintaining current threat intelligence is critical.
    </li>
    <li>
      Deploying open-source security tools is a valuable alternative for individuals or organizations without the budget for commercial solutions or those just beginning to address information security. However, it is important to recognize that the responsibility for information security when using such tools falls entirely on the user.
    </li>
    <li>
      One must bear in mind that some open-source security solutions may not offer the same level of protection as commercial alternatives — such as continuous innovation, automatic updates, integration with other applications, customization, and automation. Therefore, the scope and expectations for data protection must be clearly defined.
    </li>
    <li>
      Open-source cybersecurity tools can provide strong data protection when properly used. However, it is crucial to have the knowledge and resources required to manage and maintain these tools effectively, ensuring they remain updated and operational at all times.
    </li>
  </ul>
</section>


---

## 📚 Bibliography

<ul>
  <li>
    <strong>Unveiling the Secrets of Suricata in pfSense: A Robust Shield for Your Network</strong> (2024, June 20). Tech Riders. Retrieved from: 
    <a href="https://techriders.tajamar.es/desentranando-los-secretos-de-suricata-en-pfsense-un-escudo-robusto-para-tu-red" target="_blank">
      https://techriders.tajamar.es/desentranando-los-secretos-de-suricata-en-pfsense-un-escudo-robusto-para-tu-red
    </a>
  </li>
  <li>
    <strong>IDS vs IPS: Differences Between IDS and IPS</strong>. (n.d.). Versa Networks | Spanish. Retrieved March 8, 2025, from: 
    <a href="https://versa-networks.com/es/sd-wan/ids-ips/" target="_blank">
      https://versa-networks.com/es/sd-wan/ids-ips/
    </a>
  </li>
  <li>
    Becolve Digital. (2020, July 8). <strong>IDS vs IPS: What is the Difference?</strong> Retrieved from:
    <a href="https://becolve.com/blog/ids-vs-ips-cual-es-la-diferencia/" target="_blank">
      https://becolve.com/blog/ids-vs-ips-cual-es-la-diferencia/
    </a>
  </li>
  <li>
    <strong>AMD A12-9720P Review</strong>. (n.d.). VERSUS. Retrieved March 8, 2025, from:
    <a href="https://versus.com/es/amd-a12-9720p" target="_blank">
      https://versus.com/es/amd-a12-9720p
    </a>
  </li>
  <li>
    Benitez, P. (2023, October 14). <strong>OPNsense Next-Gen Firewall: A Deep Dive into Suricata Integration</strong>. Medium. Retrieved from:
    <a href="https://medium.com/@parkerbenitez/opnsense-next-gen-firewall-a-deep-dive-into-suricata-integration-e5b71cb9b3b3" target="_blank">
      https://medium.com/@parkerbenitez/opnsense-next-gen-firewall-a-deep-dive-into-suricata-integration-e5b71cb9b3b3
    </a>
  </li>
  <li>
    Moreno, P. [@PedroMorenoBOS]. (n.d.). <strong>Video 21: PfSense Installation and Snort IDS/IPS Configuration</strong>. YouTube. Retrieved March 8, 2025, from:
    <a href="https://www.youtube.com/watch?v=cOSqHuD3-Nc" target="_blank">
      https://www.youtube.com/watch?v=cOSqHuD3-Nc
    </a>
  </li>
  <li>
    <strong>PfSense® – The World’s Most Trusted Open Source Firewall</strong>. (n.d.). Pfsense.org. Retrieved March 8, 2025, from:
    <a href="https://www.pfsense.org/" target="_blank">
      https://www.pfsense.org/
    </a>
  </li>
  <li>
    <strong>Index of /pfsense/</strong>. (n.d.). Dsu.edu. Retrieved March 8, 2025, from:
    <a href="https://repo.ialab.dsu.edu/pfsense/" target="_blank">
      https://repo.ialab.dsu.edu/pfsense/
    </a>
  </li>
  <li>
    <strong>Snort – Network Intrusion Detection & Prevention System</strong>. (n.d.). Snort.org. Retrieved March 8, 2025, from:
    <a href="https://www.snort.org/oinkcodes" target="_blank">
      https://www.snort.org/oinkcodes
    </a>
  </li>
  <li>
    De Luz, S. (2018, June 25). <strong>How to Block Thousands of Malicious IPs with the FireHOL Project</strong>. RedesZone. Retrieved from:
    <a href="https://www.redeszone.net/2018/06/25/bloquear-miles-ip-maliciosas-firehol/" target="_blank">
      https://www.redeszone.net/2018/06/25/bloquear-miles-ip-maliciosas-firehol/
    </a>
  </li>
  <li>
    Ventress, A. (n.d.). <strong>Malware: Collection of Links for Malware Analysis. Includes Automated Downloads, Workflows, and Feed Repository Creation</strong>. Liveipmap.com. Retrieved March 8, 2025, from:
    <a href="https://www.liveipmap.com/ipcomplaints" target="_blank">
      https://www.liveipmap.com/ipcomplaints
    </a>
  </li>
  <li>
    <strong>Free Tools for Networking, Development, Operations (DevOps), and Site Reliability Engineers (SRE)</strong>. (n.d.). Site24x7.com. Retrieved March 8, 2025, from:
    <a href="https://www.site24x7.com/es/tools/" target="_blank">
      https://www.site24x7.com/es/tools/
    </a>
  </li>
</ul>

