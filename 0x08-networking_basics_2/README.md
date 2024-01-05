<h1> Networking Basics Project</h1>

This project includes Bash scripts that demonstrate various networking tasks on an Ubuntu server. 
The scripts are designed to meet specific requirements and can be useful for 
educDational purposes, debugging, and network-related tasks.

<h1> 0-change_your_home_IP</h1>

<h2> Description</h2>
This script configures an Ubuntu server with the following requirements:
- Resolves localhost to 127.0.0.2
- Resolves facebook.com to 8.8.8.8

<h2> Usage</h2>
```bash
sudo ./0-change_your_home_IP
<h3>Example</h3>
# Before running the script
ping localhost
ping facebook.com

# After running the script
ping localhost
ping facebook.com

<h1>1-show_attached_IPs</h1>
<h2>Description</h2>
This script displays all active IPv4 IPs on the machine where it's executed.

<h2>Usage</h2>
./1-show_attached_IPs
<h3>Example</h3>
./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$

<h1>100-port_listening_on_localhost</h1>
<h2>Description</h2>
This script listens on port 98 on localhost using netcat. 
It demonstrates a simple connection between terminals on the same machine.
<h2>Usge<h2>
sudo ./100-port_listening_on_localhost
<h3>Example</h3>
# Terminal 0
sudo ./100-port_listening_on_localhost

# Terminal 1
telnet localhost 98
# Type some text and press Enter

# Terminal 0
# Receives the text from Terminal 1
For the sake of the exercise, this connection can be made across networks, providing a useful tool for debugging network-related issues or testing firewall rules.

Feel free to explore and modify the scripts according to your needs.
<h3>
This README file provides a brief overview of each script, how to use them, and examples of their usage. You can customize it further to include additional details or explanations depending on your project's requirements.
</h3>
