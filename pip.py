

def install_import(package,install):
	
	import importlib
	import subprocess
	if (1==1):
		
		try:
			importlib.import_module(package)
		except ImportError:
			#import pip
			subprocess.call(['pip', 'install', install])
			print("Installing package",install)
		
			








