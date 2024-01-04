# SOC Automation Homelab

## Project Description
In this project I:
- [x] Created full Wazuh instance with SOAR integration
- [x] Configured fully functional case management using TheHive
- [x] Hosted virtual machines in DigitalOcean

## Walkthrough

### Part 1 - Diagram
- The following diagram shows how our data might flow, and what pieces are required to make it all work

![diagram](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/diagram.png)

### Part 2 - Setup
- Install applications and virtual machines
  - 1 Windows 10 machine with Sysmon
  - 1 Wazuh server
  - 1 TheHive server
  - Windows 10 client PC
  - Ubuntu 22.04 for Wazuh and TheHive

Download [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and [Sysmon config file](https://github.com/olafhartong/sysmon-modular/blob/master/sysmonconfig.xml)

- Cloud hosted Ubuntu VMs on DigitalOcean, setup firewall

![firewall](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/cloud%20setup.png)

### Part 3 - Configure TheHive & Wazuh server
- Download all prerequesits for TheHive & Wazuh on VMs (as per respective website documentation)

![TheHive](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/thehive.png)

![Wazuh](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/wazuh.png)

### Part 4 - Generate telemtetry & Ingest into Wazuh
- Adjust `ossev.conf` file for Sysmon
- Download `mimikatz`, edit `ossec.conf` to log everything, then search

![search](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/wazuh%20mimikatz.png)

- Create custom rule for Sysmon

![rule](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/custom%20rules.png)

### Part 5 - Connect Shuffle
- Shuffle is our SOAR Platform
  - Security
  - Orchestration
  - Automation
  - Response

Workflow:
1. `mimikatz` alert sent to Shuffle
2. Shuffle recieves `mimikatz` alert
   1. Extract `SHA256` hash from file
3. Check reputation score with VirusTotal
4. Send details to TheHibe to create alert
5. Send email to SOC Analyst to begin investigation

![workflow](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/Shuffle%20Workflow.png)

### Response Demo
- Grab API key from Wazuh, enrich data, send email to analyst, and trigger response action

![email](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/email.png)

![api](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/api.png)

- Active response actions kicked in

![response](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/SOC%20Automation%20Homelab/active%20response.png)

## Future Considerations
In the future I could:
- automatically reset an account from active directory if a user entered their credentials on a phishing page
- contain a host if there was suspicous activity (like `mimikatz` example)


