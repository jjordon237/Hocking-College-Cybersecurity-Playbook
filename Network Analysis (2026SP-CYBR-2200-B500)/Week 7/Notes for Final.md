📍 Main Menu > CNS-352 Digital Forensics & Incident Response > Week 7 Final Project
Good — this is the right way to approach a final report. You don’t want answers, you want methodology so you can analyze each of the four PCAPs properly and write a professional report.
I’ve reviewed the Week 7 Final Project template requirements , and I’m going to give you a repeatable investigation workflow that you can use for each PCAP.
This is how a SOC analyst would approach it.
________________________________________
🔥 MASTER METHODOLOGY (Use This For All 4 PCAPs)
You will follow the same 6-phase process for each capture:
1.	Orientation
2.	Environment Mapping
3.	Baseline Analysis
4.	Anomaly Hunting
5.	Indicator Extraction
6.	Assessment & Recommendations
________________________________________
✅ PHASE 1 — Orientation (Before You Dive In)
Open the PCAP.
Immediately check:
📊 1. Protocol Hierarchy
Statistics → Protocol Hierarchy
Write down:
•	Top 5 protocols by percentage
•	Anything unusual (ex: SMB heavy, TLS heavy, DNS bursts, ICMP heavy)
This gives you your first high-level picture.
________________________________________
📡 2. Endpoints
Statistics → Endpoints → IPv4
Identify:
•	Internal IP range (10.x, 192.168.x, 172.16–31.x)
•	Top internal host by packets/bytes
•	DNS server
•	Gateway
•	Suspicious external IPs
This helps you define:
Who is likely the victim?
________________________________________
🔄 3. Conversations
Statistics → Conversations
Check:
•	TCP tab (sort by bytes + duration)
•	UDP tab (look for DNS bursts)
•	IPv4 tab (overall communication pairs)
Look for:
•	One internal IP dominating traffic
•	Long-duration sessions
•	Repeated connections to same IP
•	Large outbound data
Now you understand:
Who is talking to who and how often?
________________________________________
✅ PHASE 2 — Network Environment Overview (Section 2 of Report)
From Endpoints + Conversations, describe:
•	Internal network structure
•	Internal vs external traffic
•	DNS behavior
•	Web traffic distribution
•	Any lateral movement
Ask:
•	Is this mostly web browsing?
•	Is this workstation-heavy?
•	Is there server traffic?
•	Is there SMB between hosts?
Write this as a neutral observation section.
________________________________________
✅ PHASE 3 — Baseline Traffic (Section 3)
Now determine what “normal” looks like.
Look for:
•	Typical browsing patterns (short TLS sessions to many domains)
•	DNS lookups preceding connections
•	Internal DNS resolution
•	Internal gateway routing
Baseline questions:
•	Are there many different domains?
•	Are sessions short?
•	Are connections user-driven?
This gives you comparison criteria.
________________________________________
✅ PHASE 4 — Anomaly Hunting (Section 4)
Now actively hunt deviations.
🔍 A) Beaconing Behavior
Look for:
•	Repeated short connections to one IP
•	Consistent intervals
•	Same packet sizes
•	TLS sessions over and over
Statistics → Conversations → Sort by Duration
________________________________________
🔍 B) Large Data Transfers
Look for:
•	High outbound bytes from one host
•	High inbound executable downloads
Statistics → Conversations → Sort by Bytes
________________________________________
🔍 C) DNS Abuse
Filter:
dns
Look for:
•	High DNS volume
•	Long subdomains
•	Random domain names
•	No corresponding HTTP requests
________________________________________
🔍 D) Suspicious Ports
Check:
•	445 (SMB)
•	3389 (RDP)
•	22 (SSH)
•	4444 / high random ports
•	1194 / 51820 (VPN)
________________________________________
🔍 E) Phishing Indicators
Check:
http.request.method == "POST"
Look for:
•	login forms
•	credential parameters
•	suspicious domains
________________________________________
✅ PHASE 5 — Evidence & Indicators (Section 5)
Now extract concrete IOCs.
You should list:
•	Internal infected IP
•	External C2 IP(s)
•	Domains contacted
•	Ports used
•	Protocol patterns
•	Duration anomalies
•	Packet count anomalies
Your evidence must tie directly to:
•	A statistic view
•	A conversation view
•	A display filter result
Never guess. Always reference data.
________________________________________
✅ PHASE 6 — Analyst Assessment (Section 6)
Now answer:
•	Is this confirmed malicious?
•	Is this suspicious?
•	Is it policy violation?
•	What would you do next?
Your tone should be:
Based on observed statistical evidence...
Then recommend:
•	Isolate host
•	Pull EDR logs
•	Block external IP
•	Review DNS logs
•	Memory capture
•	Forensic imaging
________________________________________
📄 HOW TO STRUCTURE YOUR REPORT (PER PCAP)
You should NOT analyze them randomly.
Do this per PCAP:
1️⃣ Executive Summary (what happened in this capture?)
2️⃣ Network Overview
3️⃣ Baseline
4️⃣ Anomalies
5️⃣ Evidence (IOCs)
6️⃣ Assessment
Then repeat for next PCAP.
________________________________________
🧠 PRO TIP FOR A 90+ SCORE
Your instructor wants:
•	Evidence-based reasoning
•	Statistical references
•	Pattern recognition
•	Professional tone
•	No guessing
Avoid writing:
“This looks suspicious.”
Instead write:
“The Conversations view shows 10.7.15.101 maintaining repeated encrypted TCP sessions over port 443 with 23.201.27.241, with durations exceeding 3000 seconds, which deviates from normal browsing behavior.”
That’s professional.

