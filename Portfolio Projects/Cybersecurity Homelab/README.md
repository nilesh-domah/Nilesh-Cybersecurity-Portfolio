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
   
![connectivity](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/connectivity.png)

2. Configure Sysmon in Splunk [`inputs.conf`](https://www.dropbox.com/scl/fi/620i6i0o4idzrtwlqp0qp/inputs.conf?rlkey=elni2v55mpzfab72qxr5wxk3s&dl=0) file
  - Setup endpoint index in Splunk, configure Splunk Add-on for Sysmon to be able to parse data

3. Scan and Execute
  - Use Nmap to scan target machine to see what ports are open
  - Create malware
  - Disable Windows Defender
  - Execute malware to establish reverse TCP shell to see what telemetry is generated in Windows machine

![nmap](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/nmap%20results.png)

  - We will focus on `135/tcp`
  - Create malware using `msfvenom`, using the `windows/x64/meterpreter_reverse_tcp` payload

![malware](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/create%20malware.png)

  - Open up handler that will listen in on the port that we have configured in our malware using `metasploit`

![metasploit](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/metasploit.png)

  - Allow test machine to access Kali machine and download malware, then download malware onto Windows VM

![download malware](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/download%20malware.png)

4. Analyze Malware
  - Search for malware on Splunk

![search splunk](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/Cybersecurity%20Homelab/malware%20search.png)

  - We will focus on Event Code 1
  - We see that `Resume.pdf.exe` spawned `cmd.exe` with a `process_id` of 8308

![event code 1](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/splunk%20result%201.png)

![process id](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/splunk%20result%202.png)

  - We will use the `process_guid` to query our data to see what this command prompt had done

![query](https://raw.githubusercontent.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/main/Portfolio%20Projects/Cybersecurity%20Homelab/process_guid.png)

## Future Considerations
In the future, I can start creating detections to alert analysts the next time a similar activity occurs again
