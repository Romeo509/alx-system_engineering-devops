<h1> 0x0B. SSH </h1>


<h3>General</h3>

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash


#Servers are typically housed in data centers or server rooms within organizations.

#SSH stands for Secure Shell. It is a cryptographic network protocol that provides a secure way to access and manage network devices and servers over an unsecured network. SSH encrypts the communication between the client and the server, enhancing security during remote access and file transfers.


<h2>How to create an SSH RSA key pair</h2>
To create an SSH RSA key pair, you can use the ssh-keygen command, which is available on most Unix-like operating systems (including Linux and macOS) and also on Windows if you're using a tool like Git Bash. Here are the general steps:

    Open a terminal or command prompt.

    Type the following command and press Enter:

    bash

    ssh-keygen -t rsa -b 2048

    This command specifies the key type (-t rsa) and the number of bits in the key (-b 2048). You can adjust the bit value to increase the key's strength if needed.

    The command will prompt you to specify the file where you want to save the key. Press Enter to accept the default location, or provide a custom path.

    You can also set a passphrase for extra security. Press Enter if you want to skip the passphrase or enter a passphrase if you prefer.

    Note: The passphrase is an additional layer of protection. Even if someone gets access to your private key, they would still need the passphrase to use it.

    The command will generate the SSH key pair. You'll see output indicating where the keys have been saved.

    The public key is typically saved in a file with the same name as the private key but with a .pub extension.

Once the key pair is generated, you can use the private key for authentication and add the corresponding public key to the servers you want to access.

Here is a summary of the key files:

    Private Key: Typically named id_rsa (or the custom name you provided). Keep this key secure and never share it.
    Public Key: Typically named id_rsa.pub (or the custom name you provided). You can share this key with servers or services for authentication.

After generating the keys, you can use them with an SSH client to connect to servers that accept your public key for authentication.



<h2>How connect to a remote host using an SSH RSA key pair </h2>

To connect to a remote host using an SSH RSA key pair, follow these steps:

    Generate SSH Key Pair:
    If you haven't already, generate an SSH key pair using the ssh-keygen command. See the previous answer for detailed instructions.

    Copy Public Key to Remote Host:
    Copy the content of your public key (usually found in the ~/.ssh/id_rsa.pub file) to the remote host's ~/.ssh/authorized_keys file. You can use the ssh-copy-id command for this purpose:

# ssh-copy-id user@remote_host


    Replace user with your username and remote_host with the address or IP of the remote host. This command will prompt you for your user password on the remote host.

    If ssh-copy-id is not available, you can manually append the contents of your public key to the authorized_keys file on the remote host.

    SSH Connection:
    After copying the public key, you can now connect to the remote host using the private key. Use the ssh command:

#ssh -i /path/to/private/key user@remote_host
Replace /path/to/private/key with the path to your private key, user with your username, and remote_host with the address or IP of the remote host.

If your private key is located in the default location (~/.ssh/id_rsa), you can omit the -i option:

#ssh user@remote_host

    If you've set a passphrase for your private key, you'll be prompted to enter it.

    That's it! You should now be connected to the remote host using your SSH RSA key pair. Remember to keep your private key secure and not share it with others.


