# Puppet manifest to fix Apache 500 error

# Fix the issue causing the 500 error
exec { 'fix-apache-500-error':
  command     => '/bin/bash -c "sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php && service apache2 restart"',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

# Ensure Apache service is running
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Exec['fix-apache-500-error'],
}
