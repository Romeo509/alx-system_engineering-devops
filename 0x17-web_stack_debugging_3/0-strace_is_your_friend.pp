#A Puppet script to modify a line within a file on a server.

$file_to_edit = '/var/www/html/wp-settings.php'

# Puppet script to replace 'phpp' with 'php' in a file.

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
