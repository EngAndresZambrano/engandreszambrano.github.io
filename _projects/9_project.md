---
layout: page
title: Implementation of a Secure Recursive DNS Infrastructure with DNSSEC, Py-hole, Knot Resolver and VPN on Ubuntu Server
description: This project focuses on building and securing a recursive DNS infrastructure using Ubuntu Server, Py-hole, and Knot Resolver. It includes DNSSEC, blacklist-based domain filtering, DNS-over-TLS/HTTPS, and VPN integration with OpenVPN and ProtonVPN, all deployed in a virtualized network environment managed by a MikroTik router.
img: assets/img/img_title9.png
importance: 9
category: 2025 academic
---

This project explores the implementation of a secure and privacy-focused recursive DNS infrastructure within a virtualized lab environment. The network is managed through a MikroTik router, while all DNS and VPN services are hosted on Ubuntu Server machines. The DNS infrastructure includes Py-hole for ad and tracker blocking and Knot Resolver as the recursive DNS server. Security features such as DNSSEC, DNS over TLS (DoT), and DNS over HTTPS (DoH) are configured to enhance the trustworthiness and confidentiality of DNS queries.

Domain filtering is implemented via blacklist files, allowing for flexible control over allowed and blocked content. To add another layer of privacy, VPN connectivity is configured using OpenVPN and ProtonVPN, with a kill switch mechanism that prevents DNS leaks in case of connection drops.

The project also includes extensive testing phases that cover domain resolution performance, blacklist functionality, DNSSEC validation, and DNS behavior over VPN connections from both LAN and WAN devices, including mobile phones. This comprehensive setup offers a practical and robust example of secure DNS architecture in academic and experimental settings.
