<h1>Project Title: Webstack Debugging</h1>
<h3>Description</h3>

This project focuses on debugging an issue related to the Nginx configuration within an Ubuntu container. The primary goal is to ensure that Nginx is properly configured to listen on port 80 for all active IPv4 IPs.
Debugging Steps
<h3>1. Check Nginx Status</h3>
    service nginx start

<h3>2. Examine Nginx Configuration</h3>
    cat /etc/nginx/sites-available/default


