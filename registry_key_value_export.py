import os

file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/tasks/main.yml')
lines = file.readlines()

flag = False
control_ids = []

for line in lines:
    if 'win_regedit' in line:
        flag = True
        continue
    if flag:
        control_id = line.split('_')[2]
        # print(control_id)
        control_ids.append(control_id)
        flag = False

# print(control_ids)
print(len(control_ids))