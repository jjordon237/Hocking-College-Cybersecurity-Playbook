# 🧭 A+ Core 1 Online Treasure Hunt: *The Mystery of the Dead PC*

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](#)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Time](https://img.shields.io/badge/Duration-~1h45m-green.svg)](#)
[![Skills](https://img.shields.io/badge/Skills-Hardware%20•%20Networking%20•%20Virtualization%20•%20Troubleshooting-8A2BE2.svg)](#)

> Solve **10 interconnected clues** to diagnose and "repair" a failed computer system—entirely using the web, your A+ resources, and your own knowledge.  
> Work solo or in pairs. Record your answers in your **GitHub Playbook** and submit the PDF to Blackboard.

---

## 🎯 Goal
Diagnose a failed PC by following 10 clues covering **hardware, networking, virtualization, and troubleshooting**.

## 🧰 Tools
- Browser, Cengage MindTap or TestOut PC Pro, YouTube  
- Your **GitHub Playbook**

## 🔎 How It Works
1. Read each clue in order (each maps to an A+ Core 1 concept).
2. Research, verify, and record answers in your Playbook.
3. Add screenshots/command outputs where relevant.
4. Export your Playbook section to **PDF** and upload to **Blackboard**.

---

## 🔹 Clues

<details>
<summary><strong>Clue 1 – The Silent Machine</strong></summary>

**Symptoms:** No fans, lights, or beeps.  
**Prompt:** Name two root causes and the first tool you'd use to test them.

First, it is a hardware issue possibly caused by a 
faulty Power Supply unit or the motherboard due to the symptoms shown. To test it, we would 
utilize a power supply tester to determine if the PSU is delivering power to the computer. If it 
is delivering power, the motherboard is the issue.  


<summary><strong>Clue 2 – The Beeping BIOS</strong></summary>

**Symptoms:** 3 short beeps on startup.  
**Prompt:** What does this usually indicate, and what’s your next step?

The three (3) 
short beeps indicate a hardware-issue of a RAM error or malfunction. Your first steps in 
troubleshooting this problem are to check and carefully replace each RAM module to ensure 
each are seated correctly. If you test this again, you can use a multimeter to determine which 
RAM module is faulty and replace as needed.  


<summary><strong>Clue 3 – The Missing Drive</strong></summary>

**Symptoms:** BIOS says “No Boot Device Found.”  
**Prompt:** List two hardware causes and one software fix.

Two possible hardware causes for a BIOS error of “No boot device found” includes a faulty hard drive or unplugged/faulty SATA 
connectors from the hard drive to the motherboard. One software fix that could be 
implemented is to repair or reinstall your operating system. You can achieve this through 
Windows Start Up and trying to repair the drive. Alternately you can utilize bootrec /fixmbr 
and bootrec /fixboot commands to find and restore the previous boot records potentially 
stored on the hard drive. 


<summary><strong>Clue 4 – The Hot CPU</strong></summary>

**Symptoms:** Random shutdowns under load.  
**Prompt:** What component/feature prevents overheating, and how can you monitor it?

This issue points directly to the CPU overheating and performing a forced 
shutdown to avoid potential damage. The components and features used by a desktop to 
prevent overheating include thermal paste on the CPU itself, heatsinks, air-cooled fans, and 
water-cooled systems to alleviate the heat from processor use. The BIOS/UEFI also has 
software monitors of the CPU health and temperature to monitor for overheating. Various 
operating system utility programs built in can also monitor temperatures.  


<summary><strong>Clue 5 – The Slow LAN</strong></summary>

**Symptoms:** Ethernet connects but is very slow.  
**Prompt:** What command to test connectivity, and what physical layer issue could cause this?

I would start by utilizing the Ping command to determine whether the computer has 
connectivity with any website. From there you can use Ipconfig command to determine and 
configure your IPv4 address if need be. Connectivity issues can be directly affected by physical 
layer issues such as broken or frayed wires, broken connectors, misconfigured switches, 
wrong or mismatched cable type (CAT5 instead of CAT6 cables for example), or even electrical 
interference from another component touching the wires.  


<summary><strong>Clue 6 – The Phantom Display</strong></summary>

**Symptoms:** Monitor powers on but shows no image.  
**Prompt:** Two hardware causes and one isolation test.

Two possible 
hardware issues from this could include a bad connector or cable (HDMI, VGA, etc.) or a 
potential issue with the Graphics Processing Unit (GPU) failure. One simple test you can run is 
to swap out the cables and see if they or their connectors are the problem. If that is not the 
case, you can use a multimeter to determine if the GPU is receiving or sending power to the 
system. 

<summary><strong>Clue 7 – The Virtual Machine Vanishing Act</strong></summary>

**Prompt:** What file type stores a VM, and one reason for VM corruption?

The types of files used by virtual machines are completely dependant on the program you use 
for your virtual machines. For example, Hyper-V utilizes .vhd or .vhdx. Virtual Box (my 
personal favorite) utilizes .vdi while another company like VMWare uses .vmdk for their 
virtual machines. One reason for possible corruption of your virtual machine lie in how you 
closed it. If it was force-closed, it could have been corrupted.  


<summary><strong>Clue 8 – The Peripheral Puzzle</strong></summary>

**Symptoms:** USB printer detected but won’t print.  
**Prompt:** What Windows tool/setting to reset or reinstall the driver?

To troubleshoot this issue, I would utilize Windows Device Manager to uninstall/rteinstall the 
new drivers with possible updates. I could also delete and reload the printer from my 
Windows Settings program if that fails.


<summary><strong>Clue 9 – The Cloud Question</strong></summary>

**Prompt:** Identify one advantage and one risk of moving to OneDrive.

One advantage 
immediately allows the employees more access to the material anywhere, anytime if given 
access. This could dramatically speed up business as the clientele and employees can 
telecommute while still conducting business. One (very large) disadvantage of this is if the 
cloud system fails, and we have seen this happen twice in the last two months with Major 
corporations (Cloudfare and AWS), this would effectively shutter business until the cloud 
corporation repairs the connections. This also allows many more individuals potential access 
to the information as it could lead to more security leaks. This could be damning especially if 
the information is private, classified, or confidential. 


<summary><strong>Clue 10 – The Final Fix</strong></summary>

**Prompt:** Take one screenshot of a working Device Manager or `systeminfo` and include it.

<img width="1280" height="800" alt="Screenshot 2025-11-28 155353" src="https://github.com/user-attachments/assets/c50a8338-d70f-4dcf-9e37-f339149ee13d" />

I have learned a great deal hands on work to include troubleshooting techniques for various 
hardware and software issues. I plan on uising these newfound techniques to diagnose, 
repair, or replace any part, driver, or issue I come across. The biggest issue I want to correct is 
ganing more hands-on knowledge and experience.  

---

## ✅ Deliverable (Add to your Playbook)
- **All 10 numbered answers**
- **Screenshots or command outputs** (where relevant)
- **2–3 sentence reflection** on what you learned

> Export the section as **PDF** and upload to **Blackboard** before the end of lab.

---

## 🧮 Grading (100 pts)
| Category | Points |
|---|---:|
| Correct answers (10 × 7 pts) | 70 |
| Playbook documentation (organized, labeled, uploaded) | 20 |
| Professionalism & participation | 10 |

### 🔸 Optional Bonus (+5)
If you finish early:
- Design a **PCPartPicker** build under **$900** meeting small-business A+ standards.
- Add your **parts list + link** to your Playbook.

- I wholeheartedly believe that due to the current RAM shortage plaguing our country, gaining cheap and affordable RAM cards are no longer possible. Therefore, I believe using one of their pre-build computers will yield a small business an easier time. For example, this Modest AMD build boasts an AMD Ryzen 5 core, Gigabite 550 motherboard, 16 GB of Team Group DDR4 RAM, a PNY 1 TB SSD, Asus Dual Radeon RX 9060 video graphics card, and an MSI Mag PSU with a very nice case and Thermalite RBG case fans for $901.20 at the current price.

- https://pcpartpicker.com/guide/mwv6Mp/modest-amd-gaming-build

- Hurry before Microsoft, Google, IBM, Intel, and any other company utilizing AI steal the world’s supply of RAM modules.

## 📝 Notes & Attribution
- Assignment text adapted from the course handout (CC BY 4.0).  
- For an interactive version, view this repo’s **GitHub Pages** site (`index.html`).
- SAGE AI was used for help with coding said **Github Page**  

