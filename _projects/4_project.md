---
layout: page
title: Cryptography and Security - AES, TLS Certificates, and Vulnerability Assessment
description: This project explores the use of cryptographic algorithms, focusing on AES encryption, TLS certificate verification, and the vulnerabilities that arise from insecure data transmission. It includes a step-by-step guide on AES encryption, certification checks, and web security analysis.
img: assets/img/img_title4.png
importance: 4
category: academic
images:
  lightbox2: true
---


This project provides a detailed walkthrough of various cryptographic processes and security assessments in a real-world context. The focus is on AES encryption, TLS certificate verification, and web vulnerabilities.

<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/open.png" data-lightbox="standards" data-title="OPENSSL">
      <img src="/assets/img/open.png" alt="OPENSSL" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/tls.png" data-lightbox="standards" data-title="TLS">
      <img src="/assets/img/.png" alt="TLS" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/digi.png" data-lightbox="standards" data-title="Digicert">
      <img src="/assets/img/.png" alt="Digicert" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption">
    FALTA!!!!!!!!!!!!
</div>

<strong> Key topics covered in this project include:</strong>

* Algorithms Available: Using OpenSSL, the available encryption algorithms are reviewed, including the AES cipher, and commands for verifying which algorithms are active.

* Certificate Verification: Using OpenSSL commands, we verify the TLS certificates used by a live website, detailing key information such as:

* Issuer (e.g., DigiCert)

* Encryption algorithms (e.g., SHA256, RSA)

* TLS protocol versions (e.g., TLS 1.3)

* Certificate expiration and public key information.

* AES Encryption and Decryption: The project demonstrates how AES-256-CBC encryption works, explaining the process of:

* Generating encryption keys

* Creating an initialization vector (IV) for enhanced randomness

* Encrypting plaintext data using the CBC mode (Cipher Block Chaining)

* Decrypting the ciphertext back into its original form.

The process of encryption is explained step by step, and the project explores security concerns associated with AES encryption, such as vulnerabilities in the CBC mode and padding oracle attacks. The performance of AES encryption is also evaluated, measuring the time it takes to encrypt and decrypt files.

Linux User Password Hashing: The project touches on how Linux stores user passwords securely using hash functions, providing insights into the location and format of password hashes in the /etc/passwd and /etc/shadow files.

Web Security Vulnerabilities: The project investigates an insecure webpage (HTTP without TLS) and captures unencrypted credentials during a login attempt using Wireshark, showcasing the risks of not using secure protocols.

This project serves as a hands-on guide for understanding encryption techniques, verifying certificates, and identifying common vulnerabilities in cryptographic systems. It emphasizes the importance of secure data transmission and robust password management in maintaining cybersecurity.

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
