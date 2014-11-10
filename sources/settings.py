import socket

hostname = socket.gethostname()

if hostname in ('road404-dorofeev.local',):
    from config.dev import *
elif hostname in ('live'):
    from config.live import *
else:
    raise Exception("Can't load settings for host '{0}'".format(hostname))