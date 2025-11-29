# 🕵️‍♀️ Network+ Online Treasure Hunt: *The Case of the Broken Network*

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](#)
[![Time](https://img.shields.io/badge/Duration-~1h45m-green.svg)](#)
[![Skills](https://img.shields.io/badge/Skills-OSI%20Model%20•%20Subnetting%20•%20VLANs%20•%20Routing%20•%20ACLs%20•%20Monitoring-blueviolet.svg)](#)
[![Tools](https://img.shields.io/badge/Tools-Packet%20Tracer%20•%20NetAcad%20•%20Google-lightgrey.svg)](#)

> Solve 10 interconnected networking challenges to restore a broken virtual network using only  
> your **web browser**, **Cisco NetAcad Packet Tracer**, and **research skills**. :contentReference[oaicite:0]{index=0}  

---

## 🎯 Goal

Diagnose and repair a misbehaving virtual network by answering **10 sequential clues** that cover:

- OSI model & switching  
- Subnetting & addressing  
- VLANs & trunks  
- Static routing & ACLs  
- Wireless interference  
- Cabling standards  
- Layered troubleshooting  
- Network monitoring tools  

You’ll document everything in your **GitHub Playbook** and submit it as a single entry.

---

## 🧰 Tools

- Web browser  
- **Cisco Packet Tracer**  
- **Cisco NetAcad** content  
- Google / other reputable networking resources  
- Your **GitHub Playbook**

---

## 🧭 How It Works

1. Work **solo or in teams of 2–3**.
2. Follow the clues **in order** – each one builds on the last.
3. Use **Packet Tracer** to test ideas and confirm behavior where appropriate.
4. Research using **NetAcad, CompTIA Network+ objectives, and trusted tech sites**.
5. Record your answers, commands, and screenshots in a dedicated Playbook section.
6. Export that section as a **PDF** and upload it to **Blackboard** before the end of lab.

> All clues are available digitally in Blackboard — no paper handouts or QR codes needed. :contentReference[oaicite:1]{index=1}  

---

## 🔹 Clues

Each clue gives you a short scenario and a prompt. Answer concisely, but show enough detail that another technician could follow your reasoning.

---

<details>
<summary><strong>Clue 1 – The Missing Layer</strong></summary>

A switch is said to be forwarding frames, but the router never sees the traffic.

**Task:**  
- Identify **which OSI layer** this problem is most closely associated with.  
- Describe **one important function** of that layer.

*(Hint: Cisco NetAcad Ch. 2 – “Network Access”)*  
</details>

As switches are an integral part of the Data Link Layer 2 of the OSI model, and since this switch is not correctly forwarding the frames, I believe the Data Link Layer is where he has the issue. One function of the Data Link Layer is called frame forwarding which uses MAC addresses to forward frames to the appropriate address. It also has error detection through various protocols. 

<details>
<summary><strong>Clue 2 – The Address Mystery</strong></summary>

Your subnet is **192.168.50.0/26**.

**Task:**  
- First usable host: 192.168.50.1
- Last usable host: 192.168.50.62
- Broadcast address: 192.168.50.63

</details>

---

<details>
<summary><strong>Clue 3 – The Silent VLAN</strong></summary>

In Packet Tracer you have created **VLAN 20**, but PCs in that VLAN still cannot communicate.

**Task:**  
- List **two Cisco IOS commands** you would run to verify:  
  - VLAN existence/ports  
  - Trunk status and allowed VLANs  
</details>

When dealing with unruly computers in Packet Tracer that cannot connect, you can utilize two specific commands “show vlan brief” and “show interfaces trunk”. The “show vlan brief” command allows the user to see all VLANs that currently are on the switch. This command either confirms or denies whether VLAN 20 exists and which ports are assigned to it. The “show interface trunk” command allows the user to dig deeper and see which interfaces are operating the trunks. This command will either confirm or deny whether VLAN 20 is allowed across the trunk link.
<details>
<summary><strong>Clue 4 – The Lost Route</strong></summary>

**Router A** cannot reach **Router B** (from **10.10.10.0/24** to **172.16.0.0/24**).

**Task:**  
- Write the **Cisco static route command** you would configure on Router A  
  (assume a /24 mask and that the next-hop IP on Router B’s side is known).  
</details>

The Cisco command that would create a static route between the routers is “ip route <destination-network> <subnet-mask> <next-hop-IP-address>”. In this case, we know the destination network as 172.16.0.0 and we can assume the subnet mask will be 255.255.255.0 due to the /24 on the Route A network. The next hop IP is the next closest IP the Router B is connected to, in this case 10.10.10.2, so we would get onto the computer Router A is on and type the command “ip route 172.16.0.0 255.255.255.0 10.10.10.2” which would, in theory, create a static route between the two routers. 

<details>
<summary><strong>Clue 5 – Ping Panic</strong></summary>

Management wants to block **all external ICMP echo requests (pings)** from crossing the edge of the network.

**Task:**  
- Write an **extended ACL entry** that denies ICMP echo traffic for “any source to any destination”.  
</details>

To configure the ACL, you would use the command “access-list 100 deny icmp any any echo”. The command “access-list” accesses the ACL. The “100” uses an extended ACL number unless you have a specific number you want to use. The “deny icmp” command blocks ICMP traffic on the network. The “any any” command would then extend the block to all sources and destinations. The “echo” command specifically blocks pings and ICMP echo requests. 

<details>
<summary><strong>Clue 6 – Wireless Whispers</strong></summary>

Users report that Wi-Fi connections are dropping randomly throughout the day.

**Task:**  
- Give **two realistic causes of wireless interference** that might explain this behavior  
  (think building materials, nearby devices, frequency overlap, etc.).  
</details>

One cause of interference that could reasonably explain the interference is the building materials such as thick or concrete walls, metal structures, underground structures, or large appliances can absorb or reflect the Wi-Fi signals. Another issue could be interference caused by other appliances using the same 2.4 GHz frequency. Some examples of this could be Bluetooth devices, baby monitors, microwaves, possibly even drones. 

<details>
<summary><strong>Clue 7 – Cable Confusion</strong></summary>

Your cable tester reports a mis-wired copper connector.

**Task:**  
- List the **correct T568B pinout color order** (positions 1–8).  
</details>

The correct order for a T568B with an RJ-45 connector is:
1.	White/Orange
2.	Orange
3.	White/Green
4.	Blue
5.	White/Blue
6.	Green
7.	White/Brown
8.	Brown


<details>
<summary><strong>Clue 8 – The Troubleshooter’s Trail</strong></summary>

A user can successfully ping their **default gateway**, but cannot ping **8.8.8.8** on the internet.

**Task:**  
- Identify **which OSI layer** you’ll test next and justify why.  
- Name at least one **command** you’d use to begin diagnosing the problem.  
</details>

In this instance, the user can ping a local gateway which confirms layers 1 and 2. The Network Layer 3 would then be the next thing to test as the user sees if the network router is forwarding the packets onto the internet as it is supposed. From there they would run the command “show ip route” to make sure it is connected and routing to 8.8.8.8. If that is confirmed, they could run “tracert 8.8.8.8” to follow the packets and see where the failure is occurring.   

<details>
<summary><strong>Clue 9 – Monitoring Mission</strong></summary>

You need to measure **bandwidth usage** and **device performance** across the network.

**Task:**  
- Identify one **network management protocol** and one **tool** you would use to collect and analyze this data  
  (Hint: CompTIA Network+ Domain 3 – Network Operations).  
</details>

While determining a Layer 3 Network issue, we would use the Simple Network Management Protocol (SNMP) to measure the network’s bandwidth by determining where the packets are being lost. We would then use Wireshark to complete a packet capture and analyze the packets to determine the bandwidth and performance. 

<details>
<summary><strong>Clue 10 – The Victory Log</strong></summary>

You’ve restored the network and verified full connectivity.

**Task:**  
- In your Playbook, create a **summary table** of all 10 clues and your answers.  
- Include **one Packet Tracer screenshot** showing a successful ping between two relevant devices.  
</details>

<img width="2559" height="1599" alt="Screenshot 2025-08-25 125745" src="https://github.com/user-attachments/assets/1b115945-f8a9-4a27-bd99-3452d60e03b0" />


## 📄 Deliverable

Create a new section in your GitHub Playbook titled:

> **“Network+ Online Treasure Hunt”**

That section should contain:

- ✅ All **10 numbered answers**  
- ✅ Any **supporting command outputs** (CLI snippets, tables, etc.)  
- ✅ At least **one Packet Tracer screenshot** for Clue 10  
- ✅ A short **reflection (2–3 sentences)** describing what you learned or which clue challenged you most  

Export just this section as a **PDF** and upload it to **Blackboard** before the end of lab. :contentReference[oaicite:2]{index=2}  

---

## 🧮 Grading (100 pts)

| Category                                         | Points |
|--------------------------------------------------|------:|
| Correct answers (10 × 7 pts each)               | 70 |
| Playbook documentation (clear, complete, neat)  | 20 |
| Professionalism & participation                 | 10 |

---

> 💡 *Tip:* Treat this like a mini incident-response report. Show the **commands you chose**, the **reasoning you applied**, and the **evidence** (screenshots/outputs) you gathered while fixing “The Case of the Broken Network”.

