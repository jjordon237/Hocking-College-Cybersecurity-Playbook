
# 🧠 Weekly Playbook Update – Week 5: Protocols & Communication

**Course:** NET-1111 – Introduction to Networks  
**Week:** 5 – Protocols & Communication  
**Student:** James Jordon  
**Date:** Week 5  

---

## 📸 Section 1 – Weekly Notes or Screenshots
<img width="619" height="1024" alt="Screenshot 2025-09-19 132400" src="https://github.com/user-attachments/assets/5074c5bc-8357-4088-b22f-04547e08173c" />

<img width="2559" height="1599" alt="Screenshot 2025-09-30 153806" src="https://github.com/user-attachments/assets/ee1208bb-cde2-4c0f-b92b-f2aee31a61f7" />

<img width="1024" height="1536" alt="88d3c444-1044-4324-b72b-e3d573388204" src="https://github.com/user-attachments/assets/5aa39773-d97b-4d88-bfb9-24cf9f942469" />

<img width="1117" height="785" alt="Screenshot 2025-10-07 125526" src="https://github.com/user-attachments/assets/eb4a9fbf-41d3-4a80-9a97-80672eff5279" />

<img width="1024" height="1536" alt="d5aee968-6ece-4809-8384-ec7a6fcaab6d" src="https://github.com/user-attachments/assets/1c50319c-9b11-4ec5-be37-946483e0839e" />

## 💡 Section 2 – Key Concepts  
### TCP vs UDP: Reliability vs Speed

**TCP (Transmission Control Protocol)** focuses on **reliability and accuracy**. It ensures data is delivered completely, in order, and without errors. TCP performs error detection, acknowledgment (ACK), and retransmission when packets are lost. It’s ideal for applications that require precision — such as **web browsing (HTTP/HTTPS)**, **email**, and **file transfers**.

**UDP (User Datagram Protocol)** prioritizes **speed and efficiency** over reliability. It sends packets (datagrams) without establishing a connection or verifying delivery. This makes UDP ideal for **real-time communication**, such as **VoIP calls**, **online gaming**, and **video streaming**, where occasional data loss is acceptable.

| Feature | TCP | UDP |
|----------|-----|-----|
| **Connection** | Connection-oriented (3-way handshake) | Connectionless (no setup) |
| **Reliability** | Reliable – delivery confirmed | Unreliable – no confirmation |
| **Error Handling** | Error detection and retransmission | Basic checksum only |
| **Speed** | Slower due to overhead | Faster, minimal overhead |
| **Typical Uses** | Web, Email, File Transfer | Streaming, Gaming, VoIP |
| **Flow Control** | Yes (windowing) | No |

**Summary Thought:**  
TCP and UDP work together to form the backbone of the internet. TCP guarantees accuracy, while UDP ensures speed — both are essential for balancing reliability and performance in modern networks.

> 💭 *Future Concept Idea:*  
> Imagine a “Multi-Phasic Data Transmission Protocol (MPDTP)” — combining TCP’s error checking with UDP’s speed, using intelligent packet tagging for adaptive delivery. This hybrid model could optimize performance for evolving network environments.

---

## 🧩 Section 3 – Applied Example  

We experience TCP and UDP every day without realizing it. For example, when attending **Collaborate meetings** with Professor Gina, the **audio and video stream** uses **UDP** — which explains occasional lag or pixelation due to dropped packets.  

Conversely, when we receive **emails or grade updates**, those rely on **TCP**, ensuring reliable and complete delivery. Without both of these protocols, the internet as we know it wouldn’t exist — and no one wants to return to the days of dial-up in 1994.

---

## 📚 Section 4 – Resources  

- [Professor Messer: Common Ports – Network+ (N10-009)](https://www.professormesser.com/network-plus/n10-009/n10-009-video/common-ports-n10-009/)  
- Cisco Networking Essentials (NetAcad, Module 15: TCP/UDP)  
- Cisco CCST Objective: *Identify and Compare Common Protocols*  

---

## ✅ Submission Checklist  

- [x] Updated Playbook on GitHub Repository  
- [x] Uploaded Week 5 screenshot & notes  
- [x] Submitted repo link in Blackboard  

---

*Prepared by James Jordon – Hocking College, Cybersecurity & Network Systems Program*  
*Assisted by Sage AI – Smart AI Guide for Education*
