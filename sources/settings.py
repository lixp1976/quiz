import socket
import re

hostname = socket.gethostname()

if re.match(r'^road404\-dorofeev(\-)?(\d+)?\.local$', hostname):
    from config.dev import *
elif hostname in ('live'):
    from config.live import *
else:
    raise Exception("Can't load settings for host '{0}'".format(hostname))