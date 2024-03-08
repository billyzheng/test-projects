import os

file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/tasks/main.yml')
lines = file.readlines()

control_ids = []

for line in lines:
    if '- name: "win_baseline_' in line:
        control_id = line.split('_')[2].strip()
        control_ids.append(control_id)
    

print(control_ids)

file.close()

