# TCP/IP Protocols & Well-Known Ports Cheat Sheet

A quick-reference guide to common TCP/IP application-layer protocols and their default ports.  
You can paste this directly into a GitHub README.md for a clean, professional look.

## Common Protocols & Ports

| Protocol / Service       | Port(s)     | Transport | Description                                      |
|--------------------------|-------------|-----------|--------------------------------------------------|
| HTTP                     | 80          | TCP       | Web traffic (unencrypted)                        |
| HTTPS                    | 443         | TCP       | Secure web traffic (TLS/SSL)                     |
| FTP (Control)            | 21          | TCP       | File Transfer Protocol – control channel         |
| FTP (Data)               | 20          | TCP       | File Transfer Protocol – data channel            |
| SFTP (over SSH)          | 22          | TCP       | Secure file transfer using SSH                   |
| FTPS (Implicit)          | 990         | TCP       | FTP over SSL/TLS (implicit)                      |
| FTPS (Explicit)          | 21          | TCP       | FTP with explicit TLS negotiation                |
| SSH                      | 22          | TCP       | Secure shell remote login & tunneling            |
| Telnet                   | 23          | TCP       | Remote terminal (insecure, legacy)              |
| SMTP                     | 25          | TCP       | Mail transfer between mail servers               |
| SMTPS (legacy)           | 465         | TCP       | SMTP over SSL (legacy)                           |
| Mail Submission          | 587         | TCP       | Client-to-server email submission (modern)       |
| POP3                     | 110         | TCP       | Post Office Protocol – download email            |
| POP3S                    | 995         | TCP       | POP3 over TLS/SSL                                |
| IMAP                     | 143         | TCP       | Internet Message Access Protocol                 |
| IMAPS                    | 993         | TCP       | IMAP over TLS/SSL                                |
| DNS                      | 53          | UDP/TCP   | Domain name lookups and zone transfers           |
| DNS over TLS (DoT)       | 853         | TCP       | Encrypted DNS over TLS                           |
| DHCP Server              | 67          | UDP       | Dynamic IP assignment – server port              |
| DHCP Client              | 68          | UDP       | Dynamic IP assignment – client port              |
| TFTP                     | 69          | UDP       | Trivial FTP (no auth, simple file transfers)     |
| NTP                      | 123         | UDP       | Network Time Protocol                            |
| SNMP                     | 161         | UDP       | Simple Network Management Protocol queries       |
| SNMP Trap                | 162         | UDP       | SNMP notifications/traps                         |
| RDP                      | 3389        | TCP/UDP   | Remote Desktop Protocol (Windows)                |
| SMB/CIFS                 | 445         | TCP       | Windows file & printer sharing                   |
| NetBIOS Name Service     | 137         | UDP       | NetBIOS name lookups                             |
| NetBIOS Datagram         | 138         | UDP       | NetBIOS datagram service                         |
| NetBIOS Session          | 139         | TCP       | NetBIOS session service                          |
| LDAP                     | 389         | TCP/UDP   | Lightweight Directory Access Protocol            |
| LDAPS                    | 636         | TCP       | LDAP over TLS/SSL                                |
| Kerberos                 | 88          | TCP/UDP   | Authentication service                           |
| Microsoft SQL Server     | 1433        | TCP       | Default SQL Server listener                      |
| MySQL                    | 3306        | TCP       | MySQL database service                           |
| PostgreSQL               | 5432        | TCP       | PostgreSQL database service                      |
| MongoDB                  | 27017       | TCP       | MongoDB database service                         |
| SIP                      | 5060        | TCP/UDP   | VoIP signaling                                   |
| SIP Secure (SIPS)        | 5061        | TCP       | SIP over TLS                                     |
| RTP / RTCP (typical)     | 5004, 5005  | UDP       | VoIP media streams (varies by implementation)    |
| IPsec (IKE / ISAKMP)     | 500         | UDP       | VPN key exchange                                 |
| IPsec NAT-T              | 4500        | UDP       | IPsec NAT traversal                              |
| L2TP                     | 1701        | UDP       | Layer 2 Tunneling Protocol                       |
| PPTP                     | 1723        | TCP       | Point-to-Point Tunneling Protocol (legacy VPN)   |
| BGP                      | 179         | TCP       | Border Gateway Protocol                          |
| Syslog                   | 514         | UDP       | System logging                                   |
| OpenVPN                  | 1194        | UDP/TCP   | OpenVPN tunnels                                  |

---

## Usage on GitHub

## SAGE AI was utilized to collate the data into the Github page. 

```markdown
[📘 TCP/IP Ports Cheat Sheet](./TCPIP-Ports-CheatSheet.md)

