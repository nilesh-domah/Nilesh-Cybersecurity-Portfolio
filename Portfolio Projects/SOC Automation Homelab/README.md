# SOC Automation Homelab

## Project Description
In this project I:
- [x] Created full Wazuh instance with SOAR integration
- [x] Configured fully functional case management using TheHive
- [x] Hosted virtual machines in DigitalOcean

## Walkthrough

### Part 1 - Diagram
The following diagram shows how our data might flow, and what pieces are required to make it all work

![diagram](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/diagram.png)

### Part 2 - Setup
Install applications and virtual machines
 - 1 Windows 10 machine with Sysmon
 - 1 Wazuh server
 - 1 TheHive server
 - Windows 10 client PC
 - Ubuntu 22.04 for Wazuh and TheHive

Download [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and [Sysmon config file](https://github.com/olafhartong/sysmon-modular/blob/master/sysmonconfig.xml)

