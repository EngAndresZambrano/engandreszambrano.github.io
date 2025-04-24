---
layout: page
title: Elastic SIEM Lab - A Practical Guide to Security Monitoring with the Elastic Stack and Kibana
description: A step-by-step lab for deploying Elastic SIEM using Kali Linux and Windows clients. Includes log integration, detection rules, and real-time dashboards with Kibana for security monitoring and analysis.
img: assets/img/img_title2.jpg
importance: 1
category: 2024 academic
giscus_comments: false
---

This project provides a step-by-step guide to deploying a fully functional Security Information and Event Management (SIEM) system using Elastic SIEM. Built in a virtualized environment, the setup includes a Kali Linux host running the Elastic Stack and multiple Windows clients acting as data sources through installed agents.

The guide covers technical requirements, the installation of Elastic components, and the integration of system and network logs. Special emphasis is placed on the use of Kibana to configure interactive dashboards for visualizing log data, monitoring system behavior, and detecting anomalies in real time.

  <div class="mt-4">
    <a href="{{ '/assets/pdf/Elastic_SIEM_Lab_Manual.pdf' | relative_url }}" class="btn btn-primary" download>
      📄 Download full PDF manual here!
    </a>
  </div>

Designed for academic use and hands-on learning, this lab provides a realistic approach to understanding how Elastic SIEM supports centralized log management, threat detection, and incident response. The implementation also explores the benefits and challenges of deploying such a system in a secure, isolated virtual environment, as demonstrated in the video below.

<div class="embed-responsive embed-responsive-16by9 mt-4 mb-4">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/1idh1V2L17U?cc_load_policy=1&cc_lang_pref=en" allowfullscreen></iframe>
</div>

The video demonstrates the use of Elastic SIEM and Kibana for real-time security monitoring and incident response. Key features include:

✅ <strong>Real-time Monitoring:</strong> Elastic SIEM enables the tracking of security events as they occur, helping to identify potential vulnerabilities such as unauthorized port scans and pings.

✅ <strong>Alert Generation:</strong> The system automatically triggers alerts for suspicious activities and sends notifications via email, facilitating quick incident response.

✅ <strong>Interactive Dashboards:</strong> Elastic SIEM offers dashboards that visualize security statistics and trends, assisting teams in detecting patterns and suspicious behavior.

✅ <strong>Active Prevention:</strong> Beyond monitoring, the system can block unauthorized actions and generate detailed incident reports, enhancing threat response capabilities.

✅ <strong>Log Integration and Analysis:</strong> The system integrates logs from various machines, allowing for comprehensive security analysis and threat detection.

These features make Elastic SIEM a powerful tool for managing and responding to security threats efficiently.

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/rulemail.png" title="Email Alert" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/triger.png" title="Triggered Alert" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="caption">
    Configuration of alert rules and resulting email notifications triggered by SIEM events.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/graph.png" title="Graph creation functionality for alert monitoring" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Graph creation functionality for alert monitoring
</div>

Real-time dashboard visualization with updated metrics for managerial decision-making.

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/triger1.png" title="Dashboard" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Real-time dashboard visualization
</div>
<h2>📚 Bibliography</h2>
<ul>
  <li>Elastic. (2025). <em>Elastic Security for SIEM</em>. Recuperado de <a href="https://www.elastic.co/security/siem" target="_blank">https://www.elastic.co/security/siem</a></li>
  <li>Elastic. (2025). <em>Documentación oficial de Elastic Stack</em>. Recuperado de <a href="https://www.elastic.co/docs" target="_blank">https://www.elastic.co/docs</a></li>
  <li>Achek, S. (2024). <em>Building a Basic SIEM with the Elastic Stack: A Step-by-Step Guide</em>. Medium. Recuperado de <a href="https://medium.com/@SamAchek/building-a-basic-siem-with-the-elastic-stack-a-step-by-setp-guide-06840fe09aa7" target="_blank">https://medium.com/@SamAchek/building-a-basic-siem-with-the-elastic-stack-a-step-by-setp-guide-06840fe09aa7</a></li>
  <li>Hannachi, H. (2024). <em>Elastic SIEM Fundamentals</em>. Medium. Recuperado de <a href="https://hassen-hannachi.medium.com/elastic-elastic-siem-fundamentals-3337d580fafe" target="_blank">https://hassen-hannachi.medium.com/elastic-elastic-siem-fundamentals-3337d580fafe</a></li>
  <li>Elastic. (2024). <em>Deploy an Elasticsearch cluster</em>. Recuperado de <a href="https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch" target="_blank">https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch</a></li>
  <li>Elastic. (2024). <em>Get started with Elastic Stack</em>. Recuperado de <a href="https://www.elastic.co/docs/get-started" target="_blank">https://www.elastic.co/docs/get-started</a></li>
  <li>Elastic. (2024). <em>Elasticsearch Service Documentation</em>. Recuperado de <a href="https://www.elastic.co/guide/en/cloud/current/index.html" target="_blank">https://www.elastic.co/guide/en/cloud/current/index.html</a></li>
  <li>Elastic. (2024). <em>Enhancements and bug fixes - January 2024</em>. Recuperado de <a href="https://www.elastic.co/guide/en/cloud/current/ec-release-notes-2024-01.html" target="_blank">https://www.elastic.co/guide/en/cloud/current/ec-release-notes-2024-01.html</a></li>
  <li>Elastic. (2024). <em>Elastic Accelerates SIEM Data Onboarding with Automatic Import Powered by Search AI</em>. Recuperado de <a href="https://ir.elastic.co/news/news-details/2024/Elastic-Accelerates-SIEM-Data-Onboarding-with-Automatic-Import-Powered-by-Search-AI/default.aspx" target="_blank">https://ir.elastic.co/news/news-details/2024/Elastic-Accelerates-SIEM-Data-Onboarding-with-Automatic-Import-Powered-by-Search-AI/default.aspx</a></li>
  <li>Logit.io. (2024). <em>Complete Guide To ELK</em>. Recuperado de <a href="https://logit.io/blog/post/elk-stack-guide/" target="_blank">https://logit.io/blog/post/elk-stack-guide/</a></li>
</ul>


