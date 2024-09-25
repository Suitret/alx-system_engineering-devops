# Puppet manifest to fix Apache 500 error caused by missing PHP modules or incorrect permissions

exec {'fix error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
