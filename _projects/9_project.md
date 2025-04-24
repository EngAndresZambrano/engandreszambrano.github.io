---
layout: page
title: Implementation of a Secure Recursive DNS Infrastructure with DNSSEC, Py-hole, Knot Resolver and VPN on Ubuntu Server
description: This project focuses on building and securing a recursive DNS infrastructure using Ubuntu Server, Py-hole, and Knot Resolver. It includes DNSSEC, blacklist-based domain filtering, DNS-over-TLS/HTTPS, and VPN integration with OpenVPN and ProtonVPN, all deployed in a virtualized network environment managed by a MikroTik router.
img: assets/img/img_title9.png
importance: 9
category: 2025 academic
images:
  lightbox2: true
---

This project explores the implementation of a secure and privacy-focused recursive DNS infrastructure within a virtualized lab environment. The network is managed through a MikroTik router, while all DNS and VPN services are hosted on Ubuntu Server machines. The DNS infrastructure includes Py-hole for ad and tracker blocking and Knot Resolver as the recursive DNS server. Security features such as DNSSEC, DNS over TLS (DoT), and DNS over HTTPS (DoH) are configured to enhance the trustworthiness and confidentiality of DNS queries.

Domain filtering is implemented via blacklist files, allowing for flexible control over allowed and blocked content. To add another layer of privacy, VPN connectivity is configured using OpenVPN and ProtonVPN, with a kill switch mechanism that prevents DNS leaks in case of connection drops.

The project also includes extensive testing phases that cover domain resolution performance, blacklist functionality, DNSSEC validation, and DNS behavior over VPN connections from both LAN and WAN devices, including mobile phones. This comprehensive setup offers a practical and robust example of secure DNS architecture in academic and experimental settings.

---

<h2>🛠️ Environment Prerequisites and Network Diagram</h2>
<p>This section outlines the software and hardware requirements, as well as a high-level diagram of the virtual network setup involving DNS servers, VPN nodes, and MikroTik router configuration.</p>

<table class="table table-bordered">
  <thead class="table-light">
    <tr>
      <th colspan="2" class="text-center">Hardware</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Description</td>
      <td>Characteristics</td>
    </tr>
    <tr>
      <td>Asus Equipment</td>
      <td>X510QA</td>
    </tr>
    <tr>
      <td>RAM</td>
      <td>12 GB</td>
    </tr>
    <tr>
      <td>Processor AMD A12</td>
      <td>4 cores</td>
    </tr>
    <tr>
      <td>Disk</td>
      <td>SSD 500 GB</td>
    </tr>

    <tr>
      <th colspan="2" class="text-center">Software – Host</th>
    </tr>
    <tr>
      <td>Operating System</td>
      <td>Windows 10</td>
    </tr>
    <tr>
      <td>VirtualBox</td>
      <td>7.1.6 r167084</td>
    </tr>

    <tr>
      <th colspan="2" class="text-center">Software – Virtualized</th>
    </tr>
    <tr>
      <td>Mikrotik</td>
      <td>Version 7.18.2</td>
    </tr>
    <tr>
      <td>Ubuntu Server</td>
      <td>Version 24.04.2</td>
    </tr>
    <tr>
      <td>Knot Resolver</td>
      <td>Version 5.7.4</td>
    </tr>
    <tr>
      <td>OpenVPN</td>
      <td>Version</td>
    </tr>
    <tr>
      <td>Kali Linux</td>
      <td>Version 2024.4</td>
    </tr>
    <tr>
      <td>Windows 10</td>
      <td>Version 22H2</td>
    </tr>
  </tbody>
</table>

<br><br>

<div class="col-sm mt-3 mt-md-0">
  <a href="/assets/img/diagp9.png" data-lightbox="standards" data-title="Network Diagram">
    <img src="/assets/img/diagp9.png" alt="Network Diagram" class="img-fluid rounded z-depth-1" />
  </a>
</div>
<div class="caption">
  Network Diagram.
</div>

---

<h2>🔐 Domain Blocking Functionality</h2>
<h3>📁 Blacklist Implementation via File</h3>
<p>Blacklists are implemented by maintaining a manually updated list of domains that should be denied resolution. The Py-hole system intercepts these requests to enforce blocking policies.</p>

<!-- Blacklist File Content (centered image with lightbox) -->
<div class="row justify-content-center mt-4">
  <div class="col-sm-6 text-center">
    <a href="/assets/img/blackp9.png" data-lightbox="blacklist" data-title="Black List">
      <img src="/assets/img/blackp9.png" alt="Black List" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption text-center">
  BlackList File Content.
</div>

---

<h2>🧪 Testing the DNS Infrastructure</h2>

<h3>🔄 Recursive DNS with Knot Resolver</h3>
<p>Tests confirm the proper functionality of Knot as a recursive DNS resolver, verifying successful query resolution through the designated upstream servers.</p>

<h3>🚫 Domain Blocking Validation</h3>
<p>This test section verifies the correct functionality of the domain blacklist by attempting to resolve blocked domains and ensuring the responses are denied or fail to resolve.</p>

<h3>⏱️ Query Response Times from the DMZ</h3>
<p>Response times are measured from a test machine located within the DMZ to evaluate performance and caching behavior.</p>

<!-- Generic Domain -->
<div class="row mt-4">
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_1g.png" data-lightbox="generic-domain" data-title="Domain Resolution Time – Generic Domain - 1st Attempt">
      <img src="/assets/img/timep9_1g.png" alt="Generic Domain - 1st Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_2g.png" data-lightbox="generic-domain" data-title="Domain Resolution Time – Generic Domain - 2nd Attempt">
      <img src="/assets/img/timep9_2g.png" alt="Generic Domain - 2nd Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">Domain Resolution Time – Generic Domain.</div>

<!-- Geo Domain -->
<div class="row mt-4">
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_1geo.png" data-lightbox="geo-domain" data-title="Domain Resolution Time – Geo Domain - 1st Attempt">
      <img src="/assets/img/timep9_1geo.png" alt="Geo Domain - 1st Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_2geo.png" data-lightbox="geo-domain" data-title="Domain Resolution Time – Geo Domain - 2nd Attempt">
      <img src="/assets/img/timep9_2geo.png" alt="Geo Domain - 2nd Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">Domain Resolution Time – Geo Domain.</div>

<!-- Third Level Domain -->
<div class="row mt-4">
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_1tl.png" data-lightbox="third-level-domain" data-title="Domain Resolution Time – Third Level Domain - 1st Attempt">
      <img src="/assets/img/timep9_1tl.png" alt="Third Level Domain - 1st Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    <a href="/assets/img/timep9_2tl.png" data-lightbox="third-level-domain" data-title="Domain Resolution Time – Third Level Domain - 2nd Attempt">
      <img src="/assets/img/timep9_2tl.png" alt="Third Level Domain - 2nd Attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">Domain Resolution Time – Third Level Domain.</div>

---
<h3>📱 DNS Query Testing from WAN via Mobile Device</h3>
<p>Testing involves connecting a smartphone from an external WAN and verifying DNS functionality using tools like Termux and command-line utilities. Query behavior under restrictive conditions is also explored.</p>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/phone1p9.png" title="DNS Server Config" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/phone2p9.png" title="Domain Resolution" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
---
<h3>🛡️ DNSSEC Validation</h3>
<p>This stage evaluates DNSSEC verification for signed domains, ensuring that responses are authenticated and integrity-protected throughout recursive resolution.</p>

<div class="row justify-content-center mt-4">
  <div class="col-sm-6 mt-3 mt-md-0 text-center">
    <a href="/assets/img/dnssec.png" data-lightbox="dnssec" data-title="DNSSEC Test">
      <img src="/assets/img/dnssec.png" alt="DNSSEC Test" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption text-center">
  DNSSEC Validation with sigok web.
</div>

---
<h2>🧩 Additional Activity: VPN Integration</h2>

<h3>🔒 ProtonVPN and Kill Switch with OpenVPN</h3>
<p>ProtonVPN is configured alongside OpenVPN to ensure encrypted traffic tunnels. A kill switch mechanism is implemented to halt traffic if the VPN connection drops, preventing DNS and IP leakage.</p>
---
<h3>📶 DNS Testing Over VPN from LAN</h3>
<p>Testing verifies that DNS queries from inside the LAN are routed through the VPN tunnel and do not leak through default routes.</p>

<div class="row mt-4">
  <div class="col-sm mt-3 mt-md-0 text-center">
    <a href="/assets/img/ipp91.png" data-lightbox="vpn" data-title="VPN Public IP">
      <img src="/assets/img/ipp91.png" alt="VPN Public IP" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0 text-center">
    <a href="/assets/img/ipp92.png" data-lightbox="vpn" data-title="DNS BlackList Block over VPN">
      <img src="/assets/img/ipp92.png" alt="DNS BlackList Block over VPN" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="row mt-4">
  <div class="col-sm mt-3 mt-md-0 text-center">
    <a href="/assets/img/pingp91.png" data-lightbox="vpn" data-title="Ping and Traffic Stops with Down Tunnel">
      <img src="/assets/img/pingp91.png" alt="Ping and Traffic Stops with Down Tunnel" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0 text-center">
    <a href="/assets/img/pingp92.png" data-lightbox="vpn" data-title="Tunnel Stopped">
      <img src="/assets/img/pingp92.png" alt="Tunnel Stopped" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

---

<h2>🎞️ Demo Video Showing the Results of the Script</h2>
<div class="embed-responsive embed-responsive-16by9 mt-4 mb-4">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/tF_GO8xAynw" allowfullscreen></iframe>
</div>

---

<h2>📌 Conclusions</h2>
<p>The project successfully demonstrates how to deploy and secure a recursive DNS infrastructure using open-source tools. It covers core security mechanisms such as DNSSEC, DNS filtering, and encrypted DNS transport, along with privacy enhancement through VPN integration. These findings serve as a valuable blueprint for educational, research, and practical deployments of DNS services in secure environments.</p>

<p>Based on the results from the tests conducted with the recursive DNS server, it can be concluded that although the response times, particularly for third-level domains, are high (an average of 2500 milliseconds), they decrease significantly (ranging from 25 to 0 milliseconds) when repeated queries are made due to caching. Therefore, it is recommended to properly configure this parameter to obtain much faster responses. Following the same premise, it is worth noting that the inclusion of DNSSEC enhances the speed of recursive resolution by adding a security layer that prevents responses from poisoned servers or attacks in transit.</p>

<p>During the activity, tests were conducted with three different VPNs: WireGuard with Nullvad, NordVPN with OpenVPN, and ProtonVPN with OpenVPN. Based on this experience, it is important to assert that the selection of a VPN depends on multiple factors, with key considerations being its usability, compatibility, reliability, and accessibility. In this particular case, ProtonVPN was found to be the most suitable and was implemented due to its greater flexibility in the free license, which provides accessibility. Additionally, it meets the requirements for an academic project, is compatible with Ubuntu Server, and is reliable, offering a wide range of available servers along with uptime statistics.</p>

<p>Based on the experience gained from implementing the VPN in the network, it is important to emphasize that although all VPNs provide the advantage of traffic encryption, several key technical considerations must be taken into account when acquiring and implementing one. Special attention should be given to the provider and its specifications. This includes investigating the support offered by the provider, the quality of the uptime for the servers they offer, the type of authentication available to users (dynamic and static keys, user and password authentication), and compatibility with the network's services, hardware, and software where the solution will be implemented.</p>

---

<h2>📚 Bibliography</h2>
<ul>
  <li><a href="https://es.wikipedia.org/wiki/Sistema_de_nombres_de_dominio">Wikipedia - DNS</a></li>
  <li><a href="https://www.redeszone.net/noticias/seguridad/practicas-seguridad-dns-implementar/">RedesZone - DNS Security</a></li>
  <li><a href="https://www.kaspersky.es/blog/secure-dns-private-dns-benefits/28454/">Kaspersky - Secure DNS</a></li>
  <li><a href="https://www.cloudflare.com/es-es/learning/dns/dns-over-tls/">Cloudflare - DNS over TLS</a></li>
  <li><a href="https://www-cloudns-net.translate.goog/blog/understanding-dot-and-doh-dns-over-tls-vs-dns-overhttps/">ClouDNS - DoT vs DoH</a></li>
  <li><a href="https://kinsta.com/es/base-de-conocimiento/que-es-dns/">Kinsta - What is DNS</a></li>
  <li><a href="https://www.digicert.com/es/faq/dns/recursive-and-authoritative-dns-differences">DigiCert - DNS Types</a></li>
  <li><a href="https://www.knot-resolver.cz/">Knot Resolver Official</a></li>
  <li><a href="https://elpuig.xeill.net/Members/vcarceler/articulos/introduccion-a-knot-resolver">El Puig - Knot Intro</a></li>
  <li><a href="https://phoenixnap.com/kb/powerdns-ubuntu">PowerDNS on Ubuntu</a></li>
  <li><a href="https://nordvpn.com/servers/tools/">NordVPN Tools</a></li>
  <li><a href="https://protonvpn.com/">ProtonVPN Official</a></li>
</ul>
