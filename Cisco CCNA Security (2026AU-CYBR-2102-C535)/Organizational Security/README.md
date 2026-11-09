# Organizational Security

## SOC Analyst Casebook — Investigation Scope and Evidence Plan

**Course:** NetAcad Data and Tools  
**Training environment:** Frothly / Wonderland SOC (course-provided scenario)  
**Project stage:** Milestone 1 — Planning  
**Status:** Investigation plan; endpoint execution **not confirmed**

> **Training-only project:** This casebook uses indicators supplied in coursework. The investigation is a planned exercise, not a claim that Frothly or any real organization was compromised.

## Overview

This section documents an entry-level SOC investigation plan focused on a specific question:

**What evidence would a SOC analyst need to determine whether a suspicious file associated with Warzone RAT/AveMaria executed on an endpoint, rather than being only downloaded, detected, or blocked before execution?**

Three course-provided hashes are used as malware-research examples. Warzone RAT/AveMaria is the main working example; Mirai and Emotet provide supporting comparisons. The goal is to learn how to distinguish **file reputation**, **observed execution**, and **confirmed impact** using evidence.

## What I Did / Investigation Scope

- Reviewed three hash indicators supplied by the NetAcad Data and Tools activity.
- Practiced researching malware associations using publicly available threat-intelligence information.
- Defined a plan to compare antivirus/endpoint alerts, process activity, and network records **if supplied through the authorized Frothly activities**.
- Identified missing evidence rather than assuming a file executed or infected a system.

**In scope:** Course-provided hash indicators, public threat-intelligence context, and any relevant logs or alerts explicitly supplied for the Frothly training scenario.

**Out of scope:** Production systems, unauthorized access, running live malware, advanced reverse engineering, attacker attribution, and claims of infection unsupported by training evidence.

## Evidence Plan

| Evidence type / source | Fields or details to inspect | Question answered | Status and limitations |
| --- | --- | --- | --- |
| **Course-provided file hashes** — NetAcad activity | Exact hash value; possible algorithm; source of indicator | Which sample are we researching? | **Available.** Hashes alone do not show whether a file existed or ran on a Frothly endpoint. |
| **Public threat intelligence** — VirusTotal and relevant published reports | Detection labels, reported family, report date, source | What is publicly reported about the sample? | **Research started.** Classifications require source checking and do not prove local execution. |
| **Antivirus / security alerts** — assigned Frothly materials, if provided | File identity, alert time, action (blocked/quarantined/allowed) | Was a threat detected or stopped? | **Not yet confirmed available.** A detection or quarantine alert does not by itself establish when execution occurred. |
| **Endpoint process activity** — assigned training logs, if provided | Process name, path, parent process, timestamps, available hash | Was the suspected program recorded as starting? | **Not yet confirmed available.** Missing process logs cannot prove that execution never happened. |
| **Network / authentication records** — assigned training logs, if provided | Source/destination, protocol, port, account, timestamp | Was there related suspicious traffic or account activity? | **Not yet confirmed available.** Connections alone do not prove malware execution or lateral movement. |

### Course hash references

These hashes are training indicators, **not confirmed Frothly endpoint detections**:

| Training example | Hash type | Hash |
| --- | --- | --- |
| Mirai-associated example | SHA-256-shaped | `0d1bc013bcf23de96590a57fbac2f54f239a21602708cd2bdeed52f06930eea4` |
| Emotet-associated example (course identification; retain supporting source) | MD5-shaped | `77d5d0ac81acfbaed082d6985ffcd93f` |
| Warzone RAT / AveMaria-associated example | SHA-256-shaped | `89e0d97c3f6b79962f97e02152cff003f17d940f973d762874576dab2bc3a312` |

*Algorithm labels based on hexadecimal length are provisional until the source confirms them; record the actual analysis source when available.*

## Investigation Workflow

1. **Receive the lead:** Record the exact supplied hash, course activity, and date reviewed.
2. **Gather context:** Compare public malware-research information with NetAcad material and any assigned Frothly logs. Note sources and timestamps.
3. **Test explanations:** Consider whether the suspicious file was only identified, was blocked, or was recorded as executing. Look for agreement across records, not a single alert.
4. **Verify AI-assisted work:** Use only bounded, sanitized training information. Retain prompts and responses, verify important claims against course evidence and credible references, record corrections, and require human review. Link the actual Week 3 Activity 2.2 work record once available for publication.
5. **Document and escalate:** Separate observations, interpretations, and unknowns. Record what was checked and what remains missing. In a real SOC, refer possible execution or unresolved high-risk findings to a senior analyst following organizational procedures.

## Evidence and Findings Status

**Available now:** The three supplied hashes and the student's research notes from the NetAcad activity.

**Pending:** Confirmation of which antivirus, endpoint, network, or authentication records are included in later Frothly activities.

**Current conclusion:** The hash-research exercise provides threat context. **No conclusion about local file execution or compromise is supported without endpoint-specific evidence.**

## AI Use and Verification

AI may help define terms, organize the investigation plan, and suggest relevant evidence categories. AI output is **not** accepted as proof of malware identity, execution, or compromise.

For any AI-assisted finding, record:

- The sanitized question or prompt and AI response.
- The original source used to check the answer (such as the NetAcad work record or a malware report).
- Any correction made after verification.
- The human-reviewed conclusion.

**Week 3 Activity 2.2 record:** *Add the actual record reference or sanitized excerpt here after verifying it; do not claim an activity was completed without the record.*

## Learning

This investigation reinforces the difference between a **suspicious hash**, a **security detection**, and **evidence that a file actually executed**. It also practices recognizing missing evidence and describing uncertainty accurately.

## Professional Connection

Entry-level SOC analysts must make evidence-based assessments, preserve clear notes, and prepare useful handoffs. A clear case record helps a senior analyst understand which checks were completed and what still requires investigation.

## Documentation and Privacy

**Public location:** `Organizational-Security/` in this CCNA GitHub repository.  
**Private working notes:** *Add your actual private storage location (do not publish sensitive paths or contents).*  
**Publishable material:** Original explanations, approved course references, sanitized evidence summaries, and properly credited diagrams.  
**Do not publish:** Credentials, private identifying information, unapproved raw logs, or unreviewed sensitive screenshots.

Supporting artifacts may be cross-linked when completed:

- **System Security:** Endpoint and log-analysis documentation — *link when available*.
- **Connection Security:** Network or protocol-analysis documentation — *link when available*.

## Success Checks

- [ ] Every claim can be traced to a named course artifact or cited external source.
- [ ] Timestamps retain their dates and time zones when supplied.
- [ ] Observations, assumptions, and unanswered questions are clearly distinguished.
- [ ] Another student analyst could repeat the documented research using authorized materials.
- [ ] AI assistance and human verification are recorded.
- [ ] Only approved and sanitized content is published.

## References and Course Materials

- Cisco Networking Academy. *Data and Tools* — Frothly / Wonderland SOC training activities (course-assigned content).
- MITRE ATT&CK. [WarzoneRAT (S0670)](https://attack.mitre.org/software/S0670/).
- VirusTotal. [File-hash research portal](https://www.virustotal.com/). Cite individual reports used in the finished casebook.
- Week 3 Activity 2.2 AI verification work record — *add actual record and date*.

---

*Milestone 1 is a plan. Findings, instructor feedback, and revisions should be added in later milestones only when supported by assigned evidence.*
