from crontab import CronTab
import os
import subprocess
from logger import setup_logger

logger = setup_logger('scheduler_logger', 'log.log')

'''
CAUTION: commands are system dependent

'''

USER = 'eugene'
CODEFILE = 'actor.py'

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, CODEFILE)

# getting local python location
result = subprocess.run(['which', 'python3'], stdout=subprocess.PIPE)
pyloc = result.stdout.decode('utf-8').strip()

cron = CronTab(user=USER)
#cron.remove_all()
command = f'{pyloc} {filename}'
job = cron.new(command=command, comment='testing')
#job.day.every(1) # frequency
job.setall("00 17 * * *")

for item in cron:
    print(item)

cron.write()
