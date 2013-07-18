from hvsi.i18n import i18n_global as i18n
import hvsi.i18n, sys

file_template = """<?xml version="1.0" encoding="utf-8"?>
<resources>
%s
</resources>
"""
item_template = """	<item name="%s">%s</item>\n"""
array_template = """
	<string-array name="%s">
%s
	</string-array>
"""
array_item_template = """		<item>%s</item>"""

def parse(tree, prefix=''):
	out = ''
	prefix = prefix.decode('utf-8')
	for k in tree:
		k = k.decode('utf-8')
		if isinstance(tree[k], dict) or isinstance(tree[k], hvsi.i18n.i18n_over):
			out += parse(tree[k], prefix+ ('_' if prefix != '' else '') + k)
		elif isinstance(tree[k], list):
			result = ''
			for item in tree[k]:
				result += array_item_template % item + ('\n' if item != tree[k][-1] else '')
			result = result.decode('utf-8')
			out += array_template % (prefix+ ('_' if prefix != '' else '') + k, result)
		else:
			val = unicode(tree[k].encode('utf-8'))
			out += item_template % (prefix+ ('_' if prefix != '' else '') + k, val)
	return out

for lang in i18n:
	out = file_template % parse(i18n[lang]['app'])
	f = open(sys.argv[1], 'wb')
	f.write(out.encode('utf-8'))
	f.close()