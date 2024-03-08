import os

file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/tasks/main.yml')
lines = file.readlines()

control_ids = []

for line in lines:
    if '- name: "win_baseline_' in line:
        control_id = line.split('_')[2].strip()
        control_ids.append(int(control_id))
    

print(f'current finished tasks: {len(control_ids)}')

file.close()

control_ids.sort()

file.close()

file = open('/Users/ronechen/Ansible/test-projects/control_ids.txt')
lines = file.readlines()
lines = lines[0].split(',')
exported_control_ids = [int(x.strip()) for x in lines]
print(f'all tasks in baseline: {len(exported_control_ids)}')
for id in control_ids:
    try:
        exported_control_ids.remove(id)
    except:
        print(id)
print(f'left rate: {len(control_ids) / (len(exported_control_ids)+23)}%')
print(f'lefted items: {exported_control_ids}')