#!/usr/bin/python
from lxml import etree
f = etree.parse('nvdcve-2.0-2013.xml')
root = f.getroot()
ns = {'vuln': 'http://scap.nist.gov/schema/vulnerability/0.4'}

prods = []
for prod in root.xpath("//vuln:product[contains(text(), 'cpe:/a:oracle:mysql:')]", namespaces=ns):
    if not prod.text in prods:
        prods.append(prod.text)
prods.sort()

for prod in prods:
    cves = []
    for x in root.xpath(("//vuln:product[text()='%s']" % prod), namespaces=ns):
        cve = x.getparent().getparent().get('id')
        print("%s - %s" % (prod, cve))
        cves.append(cve)
    cve_count = len(cves)
    print("%s - Total CVEs: %d" % (prod, cve_count))
