import socket
import re

hostname = socket.gethostname()

if re.match(r'^road404\-dorofeev(\-)?(\d+)?\.local$', hostname):
    from config.dev import *
elif hostname in ('live'):
    from config.live import *
else:
    from config.dev import *
