import os
import subprocess
# export FLASK_APP=flaskr
# export FLASK_ENV=development
# flask run


os.environ['FLASK_APP'] = 'flaskr'
os.environ['FLASK_ENV'] = 'development'
os.system('pwd') 
#os.system('source /home/sojen/sojenVenv/bin/activate')
#status = os.system('flask run')
#print(status)
#subprocess.call('source /home/sojen/sojenVenv/bin/activate')
subprocess.call(['flask', 'run'])
