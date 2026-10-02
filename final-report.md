1.Scope
Taeget: scanme.nmap.org (45.33.32.156).
Date: 2026-10-02.
Tools: Nmap, nslookup, whatweb.

2. Nmap scans done
-Basic scan:nmap scanme.nmap.org -oA week3_scanme_services.
-service scan:nmap -sV -sC scanme.nmap.org -oA week3_scanme_services.

3.open ports foun
- 22/tcp open ssh 6.6.1p1 ubuntu
- 80/tcp open http apache httpd 2.4.7
- 9929/tcp open nping-echo
- 31337/tcp open tcpwrapped

4. Service table
File: nmap-output/service-table.csv generated from scanme_services.xml

5. OSINT / Web recon
- whatweb scanme.nmap.org = Apache 2.4.7 ubuntu
- nslookup =45.33.32.156

6. Risk summary
   SSH old version 6.6.1 outdated. 
   HTTP Apache 2.4.7 old.
   No critical exploit tested as per scope (recon only)

7.  Recommendations
    update Apache and openSSH, close 31337 and 9929 if not needed.
