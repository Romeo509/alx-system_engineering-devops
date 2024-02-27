# Add stable version of nginx repository
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
}

# Update software packages list
exec { 'update packages':
  command => 'apt-get update',
  require => Exec['add nginx stable repo'],
}

# Install nginx
package { 'nginx':
  ensure => 'installed',
  require => Exec['update packages'],
}

# Configure Nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html;

      location / {
        try_files \$uri \$uri/ =404;
      }

      error_page 404 /404.html;
      location  /404.html {
        internal;
      }

      location ~ /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
      }
    }
  ",
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => 'running',
  require => File['/etc/nginx/sites-enabled/default'],
}
