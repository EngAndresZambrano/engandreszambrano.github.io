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

🔐 1. Available Cipher Algorithms
By executing openssl ciphers -v, you can retrieve the list of available cipher algorithms in OpenSSL.

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/listaopenssl.png" data-lightbox="grupo1" data-title="Open SSL List">
      <img src="/assets/img/listaopenssl.png" alt="Open SSL List" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      List of available ciphers via OpenSSL.
    </p>
  </div>
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

<div class="row mt-4 text-center justify-content-center">
  <div class="col-md-5 mt-3 mt-md-0">
    <a href="/assets/img/createaes.png" data-lightbox="standards3" data-title="Create">
      <img src="/assets/img/createaes.png" alt="Create" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
  <div class="col-md-5 mt-3 mt-md-0">
    <a href="/assets/img/initaes.png" data-lightbox="standards3" data-title="Vector">
      <img src="/assets/img/initaes.png" alt="Vector" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<p class="caption mt-2 text-center">
  Private key creation. Initialization vector (IV) generation.
</p>

We use CBC (Cipher Block Chaining) for encryption.

<div class="row mt-4 justify-content-center">
  <div class="col-sm-10 text-center">
    <a href="/assets/img/block.png" data-lightbox="grupo" data-title="CCBC">
      <img src="/assets/img/block.png" alt="CCBC" class="img-fluid rounded z-depth-1" style="max-width: 60%; height: auto;" />
    </a>
    <p class="caption mt-2 text-center">
      CBC Mode Process Diagram (from GeeksForGeeks) – Image taken from 
      <a href="https://www.geeksforgeeks.org/block-cipher-modes-of-operation/" target="_blank">https://www.geeksforgeeks.org/block-cipher-modes-of-operation/</a>.
    </p>
  </div>
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

<div class="row mt-4">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/time.png" title="TIme results" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   Time measurement results.
</div>

Expected times:

1MB AES-256: ~1–5 ms

1GB AES-256: ~1–4 sec

🔑 How Linux Stores Passwords
Linux stores:

Users in /etc/passwd

Hashed passwords in /etc/shadow using secure hash functions

<div class="row mt-4">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/shadow.png" title="Shadow File" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   Hash entries in the shadow file.
</div>

⚠️ Insecure Login Example (No TLS)
The website http://divtic.net/diplomados/login/index.php lacks TLS encryption.

<div class="row mt-4">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/page.png" title="Insecure Web" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   Insecure connection warning.
</div>

After sending fake credentials (Pepe), Wireshark is used to intercept HTTP POST data.

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/login.png" data-lightbox="standards6" data-title="Login attempt">
      <img src="/assets/img/login.png" alt="Login attempt" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>

<div class="row mt-4 text-center">
  <div class="col-sm-8 mx-auto mt-3 mt-md-0">
    <a href="/assets/img/wire.png" data-lightbox="standards6" data-title="Wireshark">
      <img src="/assets/img/wire.png" alt="Wireshark" class="img-fluid rounded z-depth-1" />
    </a>
  </div>
</div>
<div class="caption">
   Login attempt with test credentials - Wireshark capture showing credentials in clear text.
</div>

📚 References
<ul>
  <li><a href="https://www.researchgate.net/figure/Cipher-block-chaining-CBC-mode-encryption_fig1_215783767" target="_blank">ResearchGate – Cipher block chaining (CBC) mode encryption</a></li>
  <li><a href="https://www.geeksforgeeks.org/block-cipher-modes-of-operation/" target="_blank">GeeksForGeeks – Block Cipher Modes of Operation</a></li>
  <li><a href="https://es.wikipedia.org/wiki/Cifrado_por_bloques#:~:text=La%20desventaja%20de%20este%20m%C3%A9todo,sea%20recomendable%20para%20protocolos%20cifrados." target="_blank">Wikipedia – Cifrado por bloques</a></li>
  <li><a href="https://en.wikipedia.org/wiki/ChaCha20-Poly1305" target="_blank">Wikipedia – ChaCha20-Poly1305</a></li>
  <li><a href="https://www.redeszone.net/2019/05/04/aes-gcm-siv-cifrado-simetrico-aead/" target="_blank">RedesZone – AES-GCM-SIV cifrado simétrico AEAD</a></li>
</ul>


