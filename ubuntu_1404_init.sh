#!/bin/bash

apt-get update
apt-get install build-essentail autoconf libtool zlib1g-dev libbz2-dev
apt-get install expect sudo

useradd -m charsyam
usermod -a -G sudo charsyam

cat <<EOF >./chpasswd1.sh
#!/usr/bin/expect -f
# wrapper to make passwd(1) be non-interactive
# username is passed as 1st arg, passwd as 2nd

set password [lindex $argv 0]

spawn passwd
expect "password:"
send "$password\r"
expect "password:"
send "$password\r"
expect eof
EOF

chmod +x ./chpasswd1.sh
./chpasswd1.sh

cat <<EOF >./chpasswd1.sh
#!/usr/bin/expect -f
# wrapper to make passwd(1) be non-interactive
# username is passed as 1st arg, passwd as 2nd

set userid [lindex $argv 1]
set password [lindex $argv 0]

spawn passwd $userid
expect "password:"
send "$password\r"
expect "password:"
send "$password\r"
expect eof
EOF

chmod +x ./chpasswd1.sh
./chpasswd1.sh
