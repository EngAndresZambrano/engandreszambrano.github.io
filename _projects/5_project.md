---
layout: page
title: Man-in-the-Middle (MitM) Attack Simulation and Defense Strategies
description: This project focuses on simulating a Man-in-the-Middle (MitM) attack within a network environment. It includes the execution of ARP spoofing to intercept traffic between a victim and a gateway, followed by methods to protect Windows and Linux systems from such attacks.
img: assets/img/img_title5.png
importance: 5
category: academic
---

🕵️‍♂️ Man-in-the-Middle Attack (MitM)
The project aims to simulate and analyze a Man-in-the-Middle (MitM) attack on a network to demonstrate its impact and potential security threats. The simulation involves the use of ARP spoofing to manipulate the Address Resolution Protocol (ARP) tables and redirect traffic from the victim machine to the attacker's machine. The attack begins with network configurations, followed by the installation of tools such as "dsniff" and "arpspoof" for traffic interception. Once the attack is initiated, network traffic is captured, including sensitive data like login credentials, using tools like Wireshark.

In addition to demonstrating the attack, the project also explores mitigation strategies, such as configuring static ARP entries and implementing network monitoring tools to detect and prevent ARP spoofing. These defense measures are tested on both Windows and Linux machines. The project provides valuable insights into how these attacks work, their potential consequences, and effective countermeasures to protect networked systems from such vulnerabilities.

🧪 Lab Setup and Initial Configuration
Based on the network topology ([Insert Figure 1 here]), we gathered the following device information:


        Device          IP Address	     MAC Address
🌐 Gateway             192.168.1.1	  80:78:71:ec:2d:10
🖥️ Victim (Windows)    192.168.1.8	  dc:f5:05:51:5a:5f
🐧 Attacker (Ubuntu)   192.168.1.9	  08:00:27:a2:52:b0

✅ Successful connectivity test was performed between attacker and victim.

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

🧼 ARP Table Flush & Packet Observation

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

🔧 Tool Installation

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

🕸️ Performing the MitM Attack
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

🛑 The victim lost internet connectivity as a result.

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
Enabled IP forwarding on the attacker’s machine to restore victim’s connectivity.
[Insert Figure 12 here]

d. Traffic Interception:
The attacker poisoned both victim and gateway ARP tables.
[Insert Figure 13 here]

Visited a non-HTTPS URL from the victim machine and entered login credentials.
[Insert Figure 14 here]

Captured plaintext credentials via Wireshark (filtered by POST packets).
[Insert Figure 15 here]

e. Attack Termination:
ARP poisoning was stopped to end the attack session.
[Insert Figure 16 here]

🛡️ Mitigation & Protection Techniques
🖥️ On Windows:
Verified MAC and IP of the gateway.

Configured a static ARP entry using netsh.
[Insert Figures 17 to 19 here]

🐧 On Ubuntu:
Similar static ARP configuration steps applied.
[Insert Figure 20 here]

🔄 Attack Reversal & Monitoring
Reverted to dynamic ARP configuration for testing purposes.
[Insert Figures 21 and 22 here]

Repeated ARP spoofing showed the attacker successfully impersonated the gateway.
[Insert Figure 23 here]

🧰 Detection Tools
Tools for ARP Spoofing detection:

NetCut Defender

WiFiman

ARP Guard (WiFi Security)

📝 Mobile Recommendations:

Use a VPN

Keep OS updated

Install security apps

Avoid public Wi-Fi

🧯 What are Anti-Sniffer & Anti-Spoofing Systems?
Anti-Sniffer:
Detects sniffing tools that capture network traffic (e.g., passwords, emails).

Anti-Spoofing:
Prevents identity falsification using techniques like:

IP verification

Email authentication

Behavior anomaly detection

🛡️ Common Techniques:

Data encryption

Firewalls

Intrusion Detection Systems (IDS)

User authentication

🏗️ Network-Level Defenses
DHCP Snooping: Validates DHCP traffic to prevent spoofing and DoS.

Port Security: Limits the number of MAC addresses per port.

Dynamic ARP Inspection (DAI): Inspects ARP packets against DHCP bindings.

MACsec: Provides Layer 2 encryption, integrity, and authentication.

Layer 2 Hardware ACLs: Filters Ethernet traffic by MAC, VLAN, and protocol type.

🔒 Recommendations:

Use strong passwords

Keep switch firmware updated

Monitor switch logs

Limit configuration access

📌 Conclusions
The weakest link in cybersecurity is often the human element.

MitM attacks are simple yet highly impactful, especially over unencrypted protocols like HTTP.

Tools like arp -a can help detect MitM attacks.

Configuring static ARP entries for gateways is a practical defense measure.


