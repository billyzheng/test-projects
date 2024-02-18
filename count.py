import time
from datetime import datetime

minute = 0
last = 0
for i in range(100000):
    file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/defaults/main.yml', 'r')
    count = 0
    lines = file.readlines()
    for line in lines:
        if 'True' in line:
            count += 1
    if count == last:
        minute += 1
    else:
        minute = 0

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f'|{dt_string}| Number of lines containing tasks: {count}, I don\'t make any changes in the last {minute} minutes :)')
    last = count
    file.close()
    time.sleep(60)
