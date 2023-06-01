import requests
requests.packages.urllib3
disable_warnings(requests.packages.urllib3.expections.InsecureRequestWarning)
def format_text(title,item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)

r = requests.get('https://manageengine:8443/',verify=False)
print(format_text('r.satus_code is: ',r.status_code))
print(format_text('r.headers is :',r.headers))
print(format_text('r.cookie is:',r.cookies))
print(format_text('r.text is:',r.text))
