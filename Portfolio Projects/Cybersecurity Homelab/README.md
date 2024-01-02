# Cybersecurity Homelab
I created my homelab in VirtualBox and did the following:
- [x] Setup a Kali attacking machine and a Windows 10 target machine
- [x] Installed Splunk and Sysmon (Olaf configuration) on Windows virtual machine (VM)
- [x] Scanned for open ports with Nmap, created and executed malware on target using msfvenom, and analyzed said malware on Splunk

![homelab](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/vmsetup.png)

## Walkthrough
1. Configure VMs - Networking
  - Make sure both Kali & Windows can 'see' each other on Internal Network

![in net](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/internal%20network.png)

  - In our scenario, we will be Analyzing Malware
  - We need to statically assign our IP addresses
    - IP address: 192.168.20.10
    - Subnet mask: 255.255.255.0
   
![connectivity](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/connectivity.png)

2. Configure Sysmon in Splunk [`inputs.conf`](https://www.dropbox.com/scl/fi/620i6i0o4idzrtwlqp0qp/inputs.conf?rlkey=elni2v55mpzfab72qxr5wxk3s&dl=0) file
3. 
