Notes: 
Task: Build a star-topology LAN in Packet Tracer and verify L2/L3 connectivity.
Steps:
1.	Select correct patch leads (straight-through PC↔switch; crossover only if no auto-MDI/MDIX). Correct patch leads chosen via the straight copper cables onto Ethernet ports as Prof. Gina showed us. Fireland Enterprises Network with switch has been shown per department.  
2.	Address hosts; verify with ping. IP Configurations were successful for all nine (9) computers, three per department. I simulated a small-office setting for a start-up software company, Fireland Enterprises. I set up the three departments with leads and techs, setting up each PC IP configuration individually. I then checked the pings from the CEO-CFO and CEO-SALES as well as SALES-R&D. Pings per computer were successful as all were checked. Two are posted below.   
 

3.	Capture screenshots of cable plan and successful pings. Successful pings are posted below, two examples.
    <img width="2559" height="1585" alt="Screenshot 2025-09-05 202021" src="https://github.com/user-attachments/assets/aa48194b-f6c6-411e-b9df-e78d46baa56a" />
<img width="2558" height="1587" alt="Screenshot 2025-09-05 160421" src="https://github.com/user-attachments/assets/46af7c32-8f1e-4a89-ab3b-4b6a35cdc294" />

 
5.	Deliverable: Packet Tracer file + 2–3 screenshots to Blackboard.
6.	SAGE prompt: “Generate a checklist to verify proper cabling and link LEDs for my Packet Tracer lab.”
7.	Explain what a star topology is, what devices are required, what connections are used, and what you had to configure on the end devices to get them connected. According to (GeeksforGeeks, 2025) a star topology for a network is a network system that consists of at least two computers and one switch, called a hub, so the computers have access to communicate with each other. There are two types of star topology, active and passive. Active star topology refers to the data transmission being regenerated as it passes through the central hub (Geeksforgeeks, 2025). Passive star topology, as those seen in home office networks, do not regenerate the data transmission between the hub and computers. (Geeksforgeeks, 2025).  The connections used between the network switch and computers are the RJ-45 ethernet links. I had to configure the specific IP4 addresses using Ipconfig /all in the terminal. From there, I could ping each IP address from another of the computers. This is advantageous as a topology in case one of the computers fail, the others can still communicate. It is more expensive than a bus topology where the computers are arranged in a row, and if one of the computers fails,  the system fails. 
🔌 Packet Tracer Cabling & LED Verification Checklist VIA SAGE ChatGPT
8.	Cable Type Selection
1.	Use straight-through (copper) cables for end device ↔ switch/router connections.
2.	Use crossover cables only when connecting like devices (switch ↔ switch, router ↔ router, PC ↔ PC).
3.	Use console cable only for CLI access to a switch/router from a PC.
8.	Port Connections
1.	Verify you’ve connected cables to the correct interfaces (e.g., FastEthernet0/0, GigabitEthernet0/1).
2.	Double-check device labels (switch ports vs router ports vs PC NIC).
9.	Link LEDs
1.	Confirm the green link light is on for each active interface.
2.	Look for amber (orange) lights—indicates negotiation/bootup; should resolve to green.
3.	If no light, re-check cable type, port status, and interface configuration.
10.	Interface Status
1.	In CLI: run show ip interface brief → all active interfaces should show up/up.
2.	If administratively down, enable with no shutdown.
11.	End-to-End Connectivity
1.	Test with ping from one device to another in the same network.
2.	If ping fails, revisit cabling, port status, and IP addressing.

“Data is not just information; it’s the thread that binds our identities to the hands that pull it.” ― Timsux Wales 
I need to practice more with how to appropriately build with Packet Tracer and how to utilize more task commands such as “ipconfig /all” for speedier set-up. I would also like more information on how to set up firewalls and maintain professional networks. 
 
 
 


