<h1>Project Title: Webstack Debugging</h1>
<h3>Description</h3>

This project focuses on debugging an issue related to the Nginx configuration within an Ubuntu container. The primary goal is to ensure that Nginx is properly configured to listen on port 80 for all active IPv4 IPs.
Debugging Steps
<h3>1. Check Nginx Status</h3>
#   service nginx start

<h3>2. Examine Nginx Configuration</h3>
#    cat /etc/nginx/sites-available/default
Verify that the Nginx configuration includes the necessary settings to listen on port 80.

<h3>3. Check for Existing Default Configuration in sites-enabled</h3>
#ls /etc/nginx/sites-enabled
Confirm if the default configuration is already enabled in the sites-enabled directory.

<h3>4. Investigate Port Binding</h3>
#netstat -tulpn | grep :80
Check if any process is already listening on port 80.

<h3>5. Verify Firewall Settings </h3>
#ufw status
#ufw allow 80

Ensure that the firewall allows traffic on port 80. Adjust firewall settings if necessary.

<h3>Bash Script to Automate the Fix</h3>
The provided Bash script (0-nginx_likes_port_80) can be used to automate the fix. It removes the default Nginx configuration, creates a symbolic link, and restarts the Nginx service.

bash

#!/usr/bin/env bash

# Check if default configuration exists
if [ -e /etc/nginx/sites-available/default ]; then
    # Remove default configuration from sites-enabled
    rm /etc/nginx/sites-enabled/default

    # Create symbolic link
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

    # Restart Nginx
    service nginx restart

    echo "Nginx configured to listen on port 80."
else
    echo "Default Nginx configuration not found."
fi

<h1>Notes</h3>

    Customize the script based on specific project requirements.
    Test the script in a controlled environment before applying it to production.
    Always consider security best practices and ensure Nginx configuration meets project needs.
