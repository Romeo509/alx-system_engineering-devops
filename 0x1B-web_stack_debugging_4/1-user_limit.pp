# Modify the OS configuration to enable login with the specified method.
#Open a file as the Holberton user without encountering any error messages.

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
