import pathlib
import re

pydir = pathlib.Path(__file__).resolve().parent
inp = pydir / 'inf-ai_c_2.svg'
oup = pydir / 'inf-ai_c_2_2.svg'

with open(inp, encoding='utf-8_sig', errors='ignore') as fr:
    text = fr.read()

replaced = ''
rc = re.compile(r'stroke-dasharray:[.\d,\s]+?;')

se = rc.search(text)
pos = 0
while se is not None:
    replaced += text[pos:pos+se.start()]
    pos = pos + se.end()
    se = rc.search(text[pos:])
replaced += text[pos:]

with open(oup, mode='w', encoding='utf-8_sig', errors='ignore') as f:
    f.write(replaced)
