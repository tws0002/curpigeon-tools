import os
import subprocess

# Return curent working directory
cwd = os.getcwd()

# Path to maya executable
maya_exec = 'C:/Program Files/Autodesk/Maya2015/bin/maya.exe'

# Semicolon separated string of all script paths 
scripts_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

# Path to qube submission script files
qube_dir = scripts_dir + '/qube'

# List of paths where maya are going to look for user preferences
maya_user_prefs = ['H:/Code/Python/kk-maya-launcher/config/user_prefs/maya', 
				   'F:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
				   'G:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
				   'J:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
				   'G:/maya',
				   '//180net1/Collab/tbertino_Curpigeon/Curpigeon_Project/Scripts/prefs/maya']

# Set up environmental variables
os.environ['MAYA_PROJECT'] = cwd
os.environ['PYTHONPATH'] = scripts_dir
os.environ['MAYA_SCRIPT_PATH'] = os.pathsep.join([scripts_dir, qube_dir])

# Iterate trough the list of user preferences directory
for path in maya_user_prefs:
	# Check if directory is exist use it
	if os.path.exists(path):
		print "User preferences", path
		os.environ['MAYA_APP_DIR'] = path
		break


# Print environment for debug
print 'Project:', os.environ['MAYA_PROJECT']
print 'User prefs:', os.environ['MAYA_APP_DIR']
print 'Python scripts:', os.environ['PYTHONPATH']
print 'Mel scripts:', os.environ['MAYA_SCRIPT_PATH']

# Run application
subprocess.Popen(maya_exec)