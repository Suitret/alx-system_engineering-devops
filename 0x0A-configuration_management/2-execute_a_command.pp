# Puppet manifest to terminate a process named "killmenow"

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
