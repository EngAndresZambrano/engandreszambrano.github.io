// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Professional CyberLab Projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "dropdown-bookshelf",
              title: "bookshelf",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/books/";
              },
            },{id: "dropdown-blog",
              title: "blog",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/blog/";
              },
            },{id: "post-google-gemini-updates-flash-1-5-gemma-2-and-project-astra",
        
          title: 'Google Gemini updates: Flash 1.5, Gemma 2 and Project Astra <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "We’re sharing updates across our Gemini family of models and a glimpse of Project Astra, our vision for the future of AI assistants.",
        section: "Posts",
        handler: () => {
          
            window.open("https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/", "_blank");
          
        },
      },{id: "post-displaying-external-posts-on-your-al-folio-blog",
        
          title: 'Displaying External Posts on Your al-folio Blog <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.open("https://medium.com/@al-folio/displaying-external-posts-on-your-al-folio-blog-b60a1d241a0a?source=rss-17feae71c3c4------2", "_blank");
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "projects-information-security-standards-and-frameworks",
          title: 'Information Security Standards and Frameworks',
          description: "This project is based on the research and presentation of the most relevant information security frameworks and policies applied within a business environment. It highlights essential standards such as NIST, ISO/IEC, and COBIT, offering a structured overview of their roles in managing cyber risks and strengthening organizational security posture.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-elastic-siem-lab-a-practical-guide-to-security-monitoring-with-the-elastic-stack-and-kibana",
          title: 'Elastic SIEM Lab - A Practical Guide to Security Monitoring with the Elastic...',
          description: "A step-by-step lab for deploying Elastic SIEM using Kali Linux and Windows clients. Includes log integration, detection rules, and real-time dashboards with Kibana for security monitoring and analysis.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-black-box-audit-report-vulnerability-assessment-with-metasploit-nessus-and-pwndoc",
          title: 'Black Box Audit Report - Vulnerability Assessment with Metasploit, Nessus, and PwnDoc',
          description: "A professional black box audit conducted on a virtual machine using tools like Metasploit, Nmap, and Nessus. The final report was structured with PwnDoc and includes technical findings, CVE exploitation, and step-by-step documentation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-cryptography-and-security-aes-tls-certificates-and-vulnerability-assessment",
          title: 'Cryptography and Security - AES, TLS Certificates, and Vulnerability Assessment',
          description: "This project explores the use of cryptographic algorithms, focusing on AES encryption, TLS certificate verification, and the vulnerabilities that arise from insecure data transmission. It includes a step-by-step guide on AES encryption, certification checks, and web security analysis.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-man-in-the-middle-mitm-attack-simulation-and-defense-strategies",
          title: 'Man-in-the-Middle (MitM) Attack Simulation and Defense Strategies',
          description: "This project focuses on simulating a Man-in-the-Middle (MitM) attack within a network environment. It includes the execution of ARP spoofing to intercept traffic between a victim and a gateway, followed by methods to protect Windows and Linux systems from such attacks.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-ids-ips-implementation-using-pfsense-and-suricata",
          title: 'IDS/IPS Implementation Using PfSense and Suricata',
          description: "This project outlines the installation, configuration, and testing of an IDS/IPS/NSM solution using PfSense for perimeter security and Suricata for intrusion detection, prevention, and network security monitoring.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-dns-script-with-ai-dns-auditing-via-prompt-engineering-and-shodan-api",
          title: 'DNS Script with AI DNS Auditing via Prompt Engineering and Shodan API',
          description: "A Python-based DNS auditing tool developed using prompt engineering with ChatGPT and the Shodan API. Designed for academic purposes, it runs in a secure virtual environment and demonstrates the use of AI in cybersecurity automation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-ssh-and-telnet-audit-application-using-shodan-api",
          title: 'SSH and Telnet Audit Application Using Shodan API',
          description: "A Python application for auditing SSH and Telnet services, leveraging the Shodan API and prompt engineering with AI. The application scans the network and exports findings in CSV format for further analysis.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-implementation-of-a-secure-recursive-dns-infrastructure-with-dnssec-py-hole-knot-resolver-and-vpn-on-ubuntu-server",
          title: 'Implementation of a Secure Recursive DNS Infrastructure with DNSSEC, Py-hole, Knot Resolver and...',
          description: "This project focuses on building and securing a recursive DNS infrastructure using Ubuntu Server, Py-hole, and Knot Resolver. It includes DNSSEC, blacklist-based domain filtering, DNS-over-TLS/HTTPS, and VPN integration with OpenVPN and ProtonVPN, all deployed in a virtualized network environment managed by a MikroTik router.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%7A%61%6E%64%72%65%73_%38%38@%68%6F%74%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/engandreszambrano", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
