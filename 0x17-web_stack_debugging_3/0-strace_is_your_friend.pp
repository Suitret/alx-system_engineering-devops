# Puppet manifest to fix Apache 500 error caused by missing PHP modules or incorrect permissions

# Ensure PHP and Apache modules are installed
package { ['php', 'libapache2-mod-php']:
  ensure => installed,
}

# Ensure correct permissions for the WordPress directory
file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Restart Apache service to apply changes
service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => Package['php'],
}

