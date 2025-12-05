# 🖥️ PC Power Failure Diagnostic Protocols  
### *A Technician’s Guide to Troubleshooting a Computer That Won’t Turn On*

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](#)
[![Category](https://img.shields.io/badge/Category-Hardware%20Troubleshooting-blue.svg)](#)
[![Skill Level](https://img.shields.io/badge/Skill%20Level-CompTIA%20A%2B%20Core%201-orange.svg)](#)
[![Made With](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](#)

---

## 🎯 **Purpose**
This document provides a complete troubleshooting protocol for diagnosing a **computer that will not power on**. It includes:
- A quick-reference bullet list  
- A full, step-by-step technician flowchart  

Use it as part of your technical troubleshooting documentation or GitHub Playbook.

---

# 🔧 **1. Quick Diagnostic Bullet List**

### **Power & POST Checks**
- Verify power cable, PSU switch, and wall outlet.
- Remove surge protector / UPS temporarily.
- Listen for **POST beeps** or watch for indicator LEDs.
- Attempt to enter BIOS/UEFI diagnostics.

### **PSU Diagnostic Protocols**
- Perform a **PSU paperclip test**.
- Use a **multimeter** to verify +12V, +5V, +3.3V rails.
- Use a dedicated **PSU tester**.
- Swap in a **known-good PSU**.

### **Component Isolation**
- Boot with only: **motherboard + CPU + PSU**.
- Add components one at a time:
  - RAM  
  - GPU  
  - Storage  
- Identify failure point by process of elimination.

### **CMOS / Firmware**
- Reset CMOS via jumper or by removing battery.
- Reseat BIOS chip if socketed (rare systems).

### **Physical Inspection**
- Look for burnt smells, bulging capacitors, or scorch marks.
- Reseat RAM, GPU, CPU power cable.
- Remove possible shorts (extra motherboard standoffs, loose screws).

### **External Device Checks**
- Unplug all USB devices.
- Try a different power cable and outlet.
- Remove docks, adapters, hubs.

---

# 🧠 **2. Full Technician Flowchart Protocol**

---

## 🔶 **Step 1 — Verify Basic Power Delivery**
1. Make sure the PSU switch is ON.  
2. Try a different known-good power cable.  
3. Bypass surge protector/UPS (common failure point).  
4. Check for motherboard standby LEDs.  
   - **No LED at all → PSU or motherboard failure likely.**

---

## 🔶 **Step 2 — Attempt to Power On**
When pressing the power button, note:
- Do any fans spin?
- Do any LEDs flash?
- Does the system shut off immediately?

**If NOTHING happens → suspect:**  
- Loose power button header  
- Dead PSU  
- Dead motherboard  

---

## 🔶 **Step 3 — Power Supply Testing**
### **Paperclip Test**
Jump PS_ON to ground and check if PSU turns on.  
If it doesn't → **PSU failure**.

### **Multimeter Testing**
Measure:
- +12V rail  
- +5V rail  
- +3.3V rail  

### **Swap Test**
Install a known-good PSU.

---

## 🔶 **Step 4 — Minimal Boot Configuration**
Disconnect everything except:
- Motherboard  
- CPU + cooler  
- PSU  
- ONE stick of RAM  

Press power.

### **Results Interpretation**
- POST beeps/lights → begin adding components  
- No response → CPU, motherboard, or short

---

## 🔶 **Step 5 — Add Components One-by-One**
Rebuild the system stepwise:
1. Add RAM → test  
2. Add GPU (if no integrated graphics) → test  
3. Add drives → test  
4. Add peripherals → test  

**Failure returns? → the last part added is faulty.**

---

## 🔶 **Step 6 — CMOS Reset**
- Use motherboard jumper  
- OR remove CMOS battery for 30 seconds

Fixes:
- No-POST due to misconfiguration  
- Boot loops  
- Wrong CPU/RAM timing issues  

---

## 🔶 **Step 7 — Physical Hardware Inspection**
Check for:
- Burnt components  
- Bulging capacitors  
- Bent CPU socket pins  
- Loose heatsink / bad thermal paste  
- Shorts caused by metal standoffs or screws touching the board  

---

## 🔶 **Step 8 — External Device Elimination**
- Unplug USB drives, webcams, printers, etc.  
- Remove hubs, docks, and adapters  
- Replace display cable & monitor (no video ≠ no boot)

---

## 🔶 **Step 9 — Evaluate Findings**
| Symptom | Likely Fault |
|--------|--------------|
| No power at all | PSU or motherboard |
| Fans spin but no POST | RAM or CPU |
| Powers on then shuts off | Overheating or PSU instability |
| POSTs but no display | GPU, monitor, or cable |
| Intermittent power | Loose connectors or short |

---

## 🔶 **Step 10 — Repair or Replace**
Based on isolation findings:
- Replace PSU  
- Replace motherboard  
- Replace faulty RAM  
- Reseat or replace CPU  
- Remove shorts or re-mount board  
- Replace GPU  

---

# 📘 **Summary**
This diagnostic protocol provides both a **quick reference** and a **deep troubleshooting procedure** for analyzing why a PC won’t power on. It mirrors industry practice and CompTIA A+ Core 1 troubleshooting workflows.

---

**AI Attribution: Information put into SAGE AI to build proper code for Github Markdown File and used to corroborate appropriate data. 
