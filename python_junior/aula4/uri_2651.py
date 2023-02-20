import re

pattern = re.compile(".*zelda", re.IGNORECASE)

link_na_carta = input()

if re.match(pattern, link_na_carta):
    print("Link Bolado")
else:
    print("Link Tranquilo")
