# Define a custom HTTP response header for Nginx
class nginx_custom_header {

  # Install Nginx
  package { 'nginx':
    ensure => installed,
  }

  # Create a custom Nginx configuration file
  file { '/etc/nginx/conf.d/custom-header.conf':
    ensure  => present,
    content => "location / {
      add_header X-Served-By $hostname;
    }",
    notify  => Service['nginx'],
  }

  # Remove the default Nginx default site configuration
  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    notify => Service['nginx'],
  }

  # Ensure Nginx is running
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Apply the nginx_custom_header class to configure Nginx with the custom header
include nginx_custom_header
