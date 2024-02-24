import json
print("Interface status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

with open('sample-data.json', 'r') as files:
    data = json.loads(files.read())
interface = data.get('imdata', [])

for i in interface:
    l1PhysIf = i.get('l1PhysIf', {})
    attr = l1PhysIf.get('attributes', {})
    dn = attr.get('dn', '')
    dsc = attr.get('descr', '')
    sp = attr.get('speed', 'inherit')
    mtu = attr.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, dsc, sp, mtu))