import re

def filter_ips(ip_add):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = re.findall(pattern, ip_add)
    return ips

text = 'The IP addresses are 192.168.1.12 and 10.0.0.1'
ips = filter_ips(text)
print(ips) # Output: ['192.168.1.1', '10.0.0.1']
