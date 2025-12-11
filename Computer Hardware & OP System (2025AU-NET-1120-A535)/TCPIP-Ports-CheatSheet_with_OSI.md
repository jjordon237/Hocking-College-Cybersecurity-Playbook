# TCP/IP Protocols & Well-Known Ports Cheat Sheet (with OSI Layers)

A complete reference chart including protocol names, ports, transport type, and OSI layer classification.

---

## ✅ Common Protocols, Their Ports, and OSI Layers

| Protocol / Service       | Port(s)     | Transport | OSI Layer | Description                                      |
|--------------------------|-------------|-----------|-----------|--------------------------------------------------|
| HTTP                     | 80          | TCP       | L7 Application | Web traffic (unencrypted)                        |
| HTTPS                    | 443         | TCP       | L7 Application | Secure web traffic (TLS/SSL)                     |
| FTP (Control)            | 21          | TCP       | L7 Application | File Transfer Protocol – control channel         |
| FTP (Data)               | 20          | TCP       | L7 Application | File transfer data channel                       |
| SFTP (over SSH)          | 22          | TCP       | L7 Application | Secure file transfer using SSH                   |
| FTPS (Implicit)          | 990         | TCP       | L7 Application | FTP over SSL/TLS                                 |
| FTPS (Explicit)          | 21          | TCP       | L7 Application | FTP with explicit TLS negotiation                |
| SSH                      | 22          | TCP       | L7 Application | Secure shell remote login & tunneling            |
| Telnet                   | 23          | TCP       | L7 Application | Remote terminal (insecure)                       |
| SMTP                     | 25          | TCP       | L7 Application | Mail transfer between servers                    |
| SMTPS (legacy)           | 465         | TCP       | L7 Application | SMTP over SSL (legacy)                           |
| Mail Submission          | 587         | TCP       | L7 Application | Authenticated outbound email                     |
| POP3                     | 110         | TCP       | L7 Application | Email download                                   |
| POP3S                    | 995         | TCP       | L7 Application | POP3 over TLS/SSL                                |
| IMAP                     | 143         | TCP       | L7 Application | Email retrieval & mailbox sync                   |
| IMAPS                    | 993         | TCP       | L7 Application | IMAP over TLS/SSL                                |
| DNS (Queries)            | 53          | UDP/TCP   | L7 Application | Domain name lookups                              |
| DNSSEC / DoT             | 853         | TCP       | L7 Application | DNS over TLS                                     |
| DHCP Server              | 67          | UDP       | L7 Application | Assigns IP addressing                            |
| DHCP Client              | 68          | UDP       | L7 Application | Receives IP configuration                        |
| TFTP                     | 69          | UDP       | L7 Application | Lightweight file transfer (no auth)              |
| NTP                      | 123         | UDP       | L7 Application | Time synchronization                             |
| SNMP                     | 161         | UDP       | L7 Application | Network monitoring                               |
| SNMP Trap                | 162         | UDP       | L7 Application | Alert notifications                               |
| RDP                      | 3389        | TCP/UDP   | L7 Application | Remote desktop                                   |
| SMB                      | 445         | TCP       | L7 Application | Windows file sharing                             |
| NetBIOS Name Service     | 137         | UDP       | L7 Application | Legacy name lookup                               |
| NetBIOS Datagram         | 138         | UDP       | L7 Application | Legacy datagram transport                        |
| NetBIOS Session          | 139         | TCP       | L7 Application | Legacy session service                           |
| LDAP                     | 389         | TCP/UDP   | L7 Application | Directory service                                |
| LDAPS                    | 636         | TCP       | L7 Application | Secure LDAP                                      |
| Kerberos                 | 88          | TCP/UDP   | L7 Application | Authentication protocol                          |
| Microsoft SQL Server     | 1433        | TCP       | L7 Application | SQL Server DB                                    |
| MySQL                    | 3306        | TCP       | L7 Application | MySQL DB                                         |
| PostgreSQL               | 5432        | TCP       | L7 Application | PostgreSQL DB                                    |
| MongoDB                  | 27017       | TCP       | L7 Application | MongoDB database                                 |
| SIP                      | 5060        | TCP/UDP   | L7 Application | VoIP signaling                                   |
| SIPS (Secure SIP)        | 5061        | TCP       | L7 Application | VoIP signaling over TLS                          |
| RTP / RTCP               | 5004–5005   | UDP       | L7 Application | Media (audio/video) transport                    |
| IPsec (IKE / ISAKMP)     | 500         | UDP       | L4 Transport | VPN key exchange                                 |
| IPsec NAT-T              | 4500        | UDP       | L4 Transport | NAT traversal for VPN                            |
| L2TP                     | 1701        | UDP       | L2 Data Link | Layer 2 tunneling                                |
| PPTP                     | 1723        | TCP       | L2/L3       | Legacy VPN tunneling                             |
| BGP                      | 179         | TCP       | L7 Application | Border Gateway Protocol (routing)                |
| Syslog                   | 514         | UDP       | L7 Application | Log forwarding                                   |
| OpenVPN                  | 1194        | UDP/TCP   | L7 Application | Modern VPN tunnels                               |

---

## 📘 Save as: `TCPIP-Ports-CheatSheet_with_OSI.md`

