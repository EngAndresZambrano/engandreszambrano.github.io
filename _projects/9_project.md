---
layout: page
title: Implementation of a Secure Recursive DNS Infrastructure with DNSSEC, Py-hole, Knot Resolver and VPN on Ubuntu Server
description: This project focuses on building and securing a recursive DNS infrastructure using Ubuntu Server, Py-hole, and Knot Resolver. It includes DNSSEC, blacklist-based domain filtering, DNS-over-TLS/HTTPS, and VPN integration with OpenVPN and ProtonVPN, all deployed in a virtualized network environment managed by a MikroTik router.
img: assets/img/img_title9.png
importance: 9
category: academic
---

This project explores the implementation of a secure and privacy-focused recursive DNS infrastructure within a virtualized lab environment. The network is managed through a MikroTik router, while all DNS and VPN services are hosted on Ubuntu Server machines. The DNS infrastructure includes Py-hole for ad and tracker blocking and Knot Resolver as the recursive DNS server. Security features such as DNSSEC, DNS over TLS (DoT), and DNS over HTTPS (DoH) are configured to enhance the trustworthiness and confidentiality of DNS queries.

Domain filtering is implemented via blacklist files, allowing for flexible control over allowed and blocked content. To add another layer of privacy, VPN connectivity is configured using OpenVPN and ProtonVPN, with a kill switch mechanism that prevents DNS leaks in case of connection drops.

The project also includes extensive testing phases that cover domain resolution performance, blacklist functionality, DNSSEC validation, and DNS behavior over VPN connections from both LAN and WAN devices, including mobile phones. This comprehensive setup offers a practical and robust example of secure DNS architecture in academic and experimental settings.

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
