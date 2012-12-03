from setuptools import setup

setup(  name='hvsi',
	version='0.1dev',
	description='HvsI webapp',
	url='http://github.com/r0ssar00/hvsi',
	author='Kevin Ross',
	author_email='r0ssar00@gmail.com',
	license='GPLv2',
	packages=['hvsi'],
	package_data = {
		'hvsi': ['requirements.txt', 'views/*.tpl','css/*.css','js/*.js','css/images/*.jpg','css/images/*.png']
	},
	exclude_package_data = {
		'hvsi': ['Countdown.jpg', 'logo.png']
	},
	install_requires=[
			'urlimport',
			'FormEncode',
			'Markdown',
			'Paste',
			'mysql-python',
			'SQLObject',
			'py-bcrypt',
			'simplejson',
			'werkzeug',
			'pytz',
			'flup'],
	extras_require = {
		'mysql': 'mysql-python'
	},
	zip_safe=True)
