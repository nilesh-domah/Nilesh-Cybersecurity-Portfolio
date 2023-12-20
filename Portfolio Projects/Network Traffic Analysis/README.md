# Network Traffic Analysis
## Project Description
This project enabled me to:
- Identify network interfaces
- Use the `tcpdump` command to capture data for inspection
- Interpret the information that `tcpdump` outputs regarding a packet
- Save and load packet data for later analysis
### Scenario
As a network analyst we will use `tcpdump` to capture and analyze live network traffic on a Linux virtual machine
### Identify Network Interfaces
- Identify the interfaces that are available:
  - `sudo ipconfig`  
  - ![pt1](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt1.png)
  - We will use `eth0` as the interface to capture network packet data
- Identify the interface options available for packet capture:
  - `sudo tcpdump -D`  
  - ![pt1.1](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt1.1.png)
  - This command allows us to identify which network interfaces are available
### Inspect the network traffic of a network interface with `tcpdump`
- Filter live network packet data from the `eth0` interface:
  - `sudo tcpdump -I eth0 -v -v5`
  - ![pt2](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt2.png)
### Capture network traffic with `tcpdump`
- Capture packet data into a file called `capture.pcap`
  - `sudo tcpdump -I eth0 -nn -c9 port 80 -w capture.pcap &`
  - ![pt3](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt3.png)
- Generate some HTTP (port 80) traffic:
  - `curl opensource.google.com`
  - ![pt3.1](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt3.1.png)
- Verify that packet data has been captured:
  - `ls -l capture.pcap`
  - ![pt3.2](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt3.2.png) 
### Filter the captured packet data
- Filter the packet header data from the capture file:
  - `sudo tcpdump -nn -r capture.pcap -v`
  - ![pt4](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt4.png)
- Filter the extended packet data from the capture file:
  - `sudo tcpdump -nn -r capture.pcap -X`
  - ![pt4.1](https://github.com/nilesh-domah/Nilesh-Cybersecurity-Portfolio/blob/main/Portfolio%20Projects/3.%20Network%20Traffic%20Analysis/pt4.1.png) 
### Test Understanding
1. What command would you use to capture 3 packets on any interface with the verbose option?
    - `sudo tcpdump -c3 -I any -v`
2. What type of information does the -v option include?
    - `-v` provides verbose information
3. What `tcpdump` command can you use to identify the interfaces that are available to perform a packet capture on?
    - `sudo tcpdump -D`
