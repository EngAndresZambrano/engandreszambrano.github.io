---
layout: page
title: Man-in-the-Middle (MitM) Attack Simulation and Defense Strategies
description: This project focuses on simulating a Man-in-the-Middle (MitM) attack within a network environment. It includes the execution of ARP spoofing to intercept traffic between a victim and a gateway, followed by methods to protect Windows and Linux systems from such attacks.
img: assets/img/img_title5.png
importance: 5
category: academic
---

<h3>🕵️‍♂️ Man-in-the-Middle Attack (MitM)</h3>
The project aims to simulate and analyze a Man-in-the-Middle (MitM) attack on a network to demonstrate its impact and potential security threats. The simulation involves the use of ARP spoofing to manipulate the Address Resolution Protocol (ARP) tables and redirect traffic from the victim machine to the attacker's machine. The attack begins with network configurations, followed by the installation of tools such as "dsniff" and "arpspoof" for traffic interception. Once the attack is initiated, network traffic is captured, including sensitive data like login credentials, using tools like Wireshark.

In addition to demonstrating the attack, the project also explores mitigation strategies, such as configuring static ARP entries and implementing network monitoring tools to detect and prevent ARP spoofing. These defense measures are tested on both Windows and Linux machines. The project provides valuable insights into how these attacks work, their potential consequences, and effective countermeasures to protect networked systems from such vulnerabilities.

<h3>🧪 Lab Setup and Initial Configuration</h3>

<table style="margin: auto; border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th>Device</th>
      <th>IP Address</th>
      <th>MAC Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🌐 Gateway</td>
      <td>192.168.1.1</td>
      <td>80:78:71:ec:2d:10</td>
    </tr>
    <tr>
      <td>🖥️ Victim (Windows)</td>
      <td>192.168.1.8</td>
      <td>dc:f5:05:51:5a:5f</td>
    </tr>
    <tr>
      <td>🐧 Attacker (Ubuntu)</td>
      <td>192.168.1.9</td>
      <td>08:00:27:a2:52:b0</td>
    </tr>
  </tbody>
</table>


<h3>✅ Successful connectivity test was performed between attacker and victim.</h3>

<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/connect1.png" data-lightbox="standards" data-title="Ping">
      <img src="/assets/img/connect1.png" alt="Ping" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/connect2.png" data-lightbox="standards" data-title="Ping Victim">
      <img src="/assets/img/connect2.png" alt="Ping Victim" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/connect3.png" data-lightbox="standards" data-title="Ping Attacker">
      <img src="/assets/img/connect3.png" alt="Ping Attacker" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<h3>🧼 ARP Table Flush & Packet Observation</h3>

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/clear.png" data-lightbox="grupo1" data-title="Clearing ARP table">
      <img src="/assets/img/clear.png" alt="Clearing ARP table" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      Cleared the ARP table on the victim machine..
    </p>
  </div>
</div>

Performed a ping from Ubuntu to Windows. The ARP request from Windows was captured using Wireshark, showing communication with the gateway and attacker IPs.

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/wirearp.png" data-lightbox="standards2" data-title="Wireshark Capture">
      <img src="/assets/img/wirearp.png" alt="Wireshark Capture" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/arp.png" data-lightbox="standards2" data-title="ARP Table">
      <img src="/assets/img/arp.png" alt="ARP Table" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<h3>🔧 Tool Installation</h3>

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/niff.png" data-lightbox="grupo2" data-title="Dsniff">
      <img src="/assets/img/niff.png" alt="Dsniff" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      Successfully installed the dsniff package.
    </p>
  </div>
</div>

<h3>🕸️ Performing the MitM Attack</h3>
a. Simulated Traffic:

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/tping.png" data-lightbox="grupo3" data-title="Continuous ping">
      <img src="/assets/img/tping.png" alt="Continuous ping" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      A continuous ping to 8.8.8.8 was sent from the Windows machine.
    </p>
  </div>
</div>

b. ARP Spoofing:

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/spoof.png" data-lightbox="grupo4" data-title="ARP Spoofing">
      <img src="/assets/img/spoof.png" alt="ARP Spoofing" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      The attacker used arpspoof -t to impersonate the gateway.
    </p>
  </div>
</div>

<h3>🛑 The victim lost internet connectivity as a result.</h3>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/lost.png" data-lightbox="standards3" data-title="ARP Spoofing">
      <img src="/assets/img/lost.png" alt="ARP Spoofing" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      The attacker used arpspoof -t to impersonate the gateway.
    </p>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/arpattk.png" data-lightbox="standards3" data-title="ARP Attack">
      <img src="/assets/img/arpattk.png" alt="ARP Attack" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      The victim’s ARP table showed the attacker’s MAC instead of the gateway’s.
    </p>
  </div>
</div>

c. IP Forwarding:

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/forw.png" data-lightbox="standards4" data-title="IP Forwarding">
      <img src="/assets/img/forw.png" alt="IP Forwarding" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Enabled IP forwarding on the attacker’s machine to restore victim’s connectivity.
    </p>
  </div>
</div>

d. Traffic Interception:

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/poison.png" data-lightbox="standards4" data-title="Poisoning">
      <img src="/assets/img/poison.png" alt="Poisoning" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      The attacker poisoned both victim and gateway ARP tables.
    </p>
  </div>
</div>
<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/page1.png" data-lightbox="standards4" data-title="non-HTTPS URL">
      <img src="/assets/img/page1.png" alt="non-HTTPS URL" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Visited a non-HTTPS URL from the victim machine and entered login credentials.
    </p>
  </div>
</div>
<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/wirehttp.png" data-lightbox="standards4" data-title="Captured plaintext">
      <img src="/assets/img/wirehttp.png" alt="Captured plaintext" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Captured plaintext credentials via Wireshark (filtered by POST packets).
    </p>
  </div>
</div>

e. Attack Termination:

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/stopoison.png" data-lightbox="standards5" data-title="Attack Stopped">
      <img src="/assets/img/stopoison.png" alt="Attack Stopped" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      ARP poisoning was stopped to end the attack session.
    </p>
  </div>
</div>

<h3>🛡️ Mitigation & Protection Techniques</h3>
<h3>🖥️ On Windows:</h3>
Verified MAC and IP of the gateway.

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/protect1.png" data-lightbox="standards6" data-title="Static ARP">
      <img src="/assets/img/protect1.png" alt="Static ARP" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Configured a static ARP entry using netsh.
    </p>
  </div>
</div>

<h3>🐧 On Ubuntu:</h3>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/neigh.png" data-lightbox="standards7" data-title="Neighbors">
      <img src="/assets/img/neigh.png" alt="Neighbors" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Similar static ARP configuration steps applied Neighbors.
    </p>
  </div>
</div>

<h3>🔄 Attack Reversal & Monitoring</h3>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/int.png" data-lightbox="standards8" data-title="Static">
      <img src="/assets/img/int.png" alt="Static" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Reverted to static ARP configuration on Victim.
    </p>
  </div>
</div>
<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/perm.png" data-lightbox="standards8" data-title="Ubuntu">
      <img src="/assets/img/perm.png" alt="Ubuntu" class="img-fluid rounded z-depth-1" />
    </a>
    <p class="caption mt-2 text-center">
      Reverted to static ARP configuration on Ubuntu.
    </p>
  </div>
</div>

<h3>🧰 Detection Tools</h3>
Tools for ARP Spoofing detection:

NetCut Defender

WiFiman

ARP Guard (WiFi Security)

<h3>📝 Mobile Recommendations:</h3>

Use a VPN

Keep OS updated

Install security apps

Avoid public Wi-Fi

<h3>🧯 What are Anti-Sniffer & Anti-Spoofing Systems?</h3>
Anti-Sniffer:
Detects sniffing tools that capture network traffic (e.g., passwords, emails).

Anti-Spoofing:
Prevents identity falsification using techniques like:

IP verification

Email authentication

Behavior anomaly detection

<h3>🛡️ Common Techniques:</h3>

Data encryption

Firewalls

Intrusion Detection Systems (IDS)

User authentication

<h3>🏗️ Network-Level Defenses</h3>
DHCP Snooping: Validates DHCP traffic to prevent spoofing and DoS.

Port Security: Limits the number of MAC addresses per port.

Dynamic ARP Inspection (DAI): Inspects ARP packets against DHCP bindings.

MACsec: Provides Layer 2 encryption, integrity, and authentication.

Layer 2 Hardware ACLs: Filters Ethernet traffic by MAC, VLAN, and protocol type.

<h3>🔒 Recommendations:</h3>

Use strong passwords

Keep switch firmware updated

Monitor switch logs

Limit configuration access

<h3>📌 Conclusions</h3>
The weakest link in cybersecurity is often the human element.

MitM attacks are simple yet highly impactful, especially over unencrypted protocols like HTTP.

Tools like arp -a can help detect MitM attacks.

Configuring static ARP entries for gateways is a practical defense measure.


