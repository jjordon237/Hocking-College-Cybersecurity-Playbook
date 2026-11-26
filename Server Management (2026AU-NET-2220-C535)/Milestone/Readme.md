[README (3).md](https://github.com/user-attachments/files/35458265/README.3.md)
# Server Management — NET2220

**James T. Jordon**

This repository contains my Server Management coursework and server project, documenting the configuration and administration of Linux and Windows Server instances in AWS EC2.

## Project Focus

- Create and manage local users and role-based groups.
- Apply least-privilege access to shared folders and files.
- Configure Linux ownership, permissions, and setgid directories.
- Configure Windows NTFS permissions with PowerShell.
- Disable retired accounts and verify account status.
- Document configuration evidence, permission tests, troubleshooting, and rollback procedures where applicable.

## Milestone 1 Files

| File | Purpose |
| --- | --- |
| [m1_linux_baseline.sh](m1_linux_baseline.sh) | Linux account, group, directory, and permission setup commands. |
| [m1_windows_baseline.ps1](m1_windows_baseline.ps1) | Windows Server account, group, directory, and NTFS permission setup commands. |
| [Jordon_M1_Baseline_Commands.txt](Jordon_M1_Baseline_Commands.txt) | Combined command reference for both operating systems. |

Project reports and supporting screenshots document the work and observed results.

## Script Use

The baseline scripts collect commands from the recorded lab setup. They have not been executed end to end as standalone scripts. Review them before use on a fresh course server; rerunning them on configured servers can change existing permissions or overwrite the sample notice. Keep the Linux and Windows command sequences separate.

## Learning Goals

Build practical server administration skills, explain access-control decisions, and connect local operating-system security with AWS IAM concepts and shared responsibility.

