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
      <img src="/assets/img/tls.png" alt="TLS" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/digi.png" data-lightbox="standards" data-title="Digicert">
      <img src="/assets/img/digi.png" alt="Digicert" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption">
    FALTA!!!!!!!!!!!!
</div>

🔐 1. Available Cipher Algorithms
By executing openssl ciphers -v, you can retrieve the list of available cipher algorithms in OpenSSL.

<div class="row mt-4">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/listaopenssl.png" title="ISO 22301" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   List of available ciphers via OpenSSL.
</div>



🌐 2. Certificate Verification in HTTPS Connections
Using openssl s_client www.avalpaycenter.com:443, we retrieve the following certificate data from a secure website.

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/cipher.png" data-lightbox="standards2" data-title="Cipher">
      <img src="/assets/img/cipher.png" alt="Cipher" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/details.png" data-lightbox="standards2" data-title="Details">
      <img src="/assets/img/details.png" alt="Details" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="caption">
   Connection and cipher information for www.avalpaycenter.com - Certificate details: TLS, SHA2, DigiCert issuer.
</div>

Key details:

Uses TLS and SHA2

Certificate issued by DigiCert Inc.

Public key: 2048-bit RSA

Signature: RSA-SHA256

TLS version: 1.3 with AES-128 and SHA256

Owner: A Toda Hora S.A (Grupo Aval)

📁 3. AES Encryption Process
We create an AES folder in the Kali desktop and proceed with private key generation.

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/createaes.png" data-lightbox="standards3" data-title="Create">
      <img src="/assets/img/createaes.png" alt="Create" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/initaes.png" data-lightbox="standards3" data-title="Vector">
      <img src="/assets/img/initaes.png" alt="Vector" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">
   Private key creation.
   Initialization vector (IV) generation.
</div>

We use CBC (Cipher Block Chaining) for encryption.

<div class="row mt-4">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/block.png" title="ISO 22301" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   CBC Mode Process Diagram (from GeeksForGeeks) - Image taken from https://www.geeksforgeeks.org/block-cipher-modes-of-operation/.
</div>

How CBC Works:

Blocks are encrypted in sequence

IV is used for randomness

XOR operation with previous cipher block

Vulnerable to padding oracle attacks

No authentication by default

⚡ ChaCha20-Poly1305 Encryption
ChaCha20: Fast stream cipher, hardware independent, 256-bit key

Poly1305: Message authentication code (MAC), ensures data integrity

Used in HTTPS, VPNs, mobile apps.

🔄 AES-GCM Mode
AES with Galois/Counter Mode for authenticated encryption.

Benefits:

No padding required

Encrypts and authenticates in one step

Ideal for modern TLS/HTTPS protocols

Secure and fast with AES-NI support

📂 Practical Encryption Example
Encrypting LABTextoClaro.txt with AES-256-CBC using:

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    <pre class="bg-dark text-white p-3 rounded">
<code class="language-bash">openssl aes-256-cbc -e -nosalt -a -kfile llave_priv.key -iv $(cat vi.key) -in LABTextoClaro.txt -out Cifrado.txt 2&gt; /dev/null</code>
</pre>
  </div>
</div>


<div class="row text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/result.png" data-lightbox="standards4" data-title="Result File">
      <img src="/assets/img/result.png" alt="Result File" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Resulting encrypted file.
    </div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/dif.png" data-lightbox="standards4" data-title="File Dif">
      <img src="/assets/img/dif.png" alt="File Dif" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      File size difference between original and encrypted.
    </div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/base64.png" data-lightbox="standards4" data-title="Base 64 Content">
      <img src="/assets/img/base64.png" alt="Base 64 Content" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Encrypted Base64 content.
    </div>
  </div>
</div>

❌ Removing Plaintext and Decrypting File
The original file is deleted and the encrypted one is decrypted:

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    <pre class="bg-dark text-white p-3 rounded">
<code class="language-bash">language-bash">openssl aes-256-cbc -d -nosalt -a -kfile llave_priv.key -iv $(cat vi.key) -in Cifrado.txt -out descifrado.txt 2&gt; /dev/null</code>
</pre>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/remove.png" data-lightbox="standards5" data-title="Delete">
      <img src="/assets/img/remove.png" alt="Delete" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Deleted plaintext file.
    </div>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm mt-3 mt-md-0">
    <a href="/assets/img/decrypt.png" data-lightbox="standards5" data-title="Decrypt">
      <img src="/assets/img/decrypt.png" alt="Decrypt" class="img-fluid rounded z-depth-1" />
    </a>
    <div class="caption mt-2">
      Decryption process.
    </div>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="/assets/img/final.png" title="Recover-Restore" class="img-fluid rounded z-depth-1" %}
    <div class="caption mt-2">
      Recovered original content - Restored original file size.
    </div>
  </div>
</div>

⏱️ Encryption Performance Benchmark
Using time to measure processing speed:

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    <pre class="bg-dark text-white p-3 rounded">
<code class="language-bash">language-bash">time openssl enc -aes-256-cbc -in Cifrado.txt -out cifradotiempo.txt -pass file:./llave_priv.key 2&gt; /dev/null</code>
</pre>
  </div>
</div>

📷 Image 15 – Time measurement results

Expected times:

1MB AES-256: ~1–5 ms

1GB AES-256: ~1–4 sec

🔑 How Linux Stores Passwords
Linux stores:

Users in /etc/passwd

Hashed passwords in /etc/shadow using secure hash functions

📷 Image 16 – Hash entries in the shadow file

⚠️ Insecure Login Example (No TLS)
The website http://divtic.net/diplomados/login/index.php lacks TLS encryption.

📷 Image 17 – Insecure connection warning

After sending fake credentials (Pepe), Wireshark is used to intercept HTTP POST data.

📷 Image 18 – Login attempt with test credentials
📷 Image 19 – Wireshark capture showing credentials in clear text

📚 References
GeeksForGeeks – Block Cipher Modes

Wikipedia – ChaCha20-Poly1305

RedesZone – AES-GCM
