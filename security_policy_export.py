import os

file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/tasks/main.yml')
lines = file.readlines()

flag = False
control_ids = []

for line in lines:
    if 'win_user_right' in line:
        flag = True
        continue
    if flag:
        control_id = line.split('_')[2]
        control_ids.append(control_id)
        flag = False

print(len(control_ids))

file.close()

# open the var.yml file
file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/defaults/main.yml')
lines = file.readlines()

print(len(lines))
test_ids = control_ids
registry_paths = []
registry_names = []
registry_data = []

# find all lines that contain id in control_ids
for line in lines:
    for control_id in control_ids:
        if 'win_baseline_' + str(control_id) + '_state_Name' in line:
            registry_names.append(line.split(': ')[-1].strip().removesuffix('\n'))
        if 'win_baseline_' + str(control_id) + '_state_Users' in line:
            registry_data.append(line.split(': ')[-1].strip().removesuffix('\n'))
            test_ids.remove(control_id)

print(len(registry_paths))
print(registry_names)
print(registry_data)

file.close()

output_file = open('security_policy_value_export.csv', 'w')
for b, c in zip(registry_names, registry_data):
    output_file.write(b + ',' + c + '\n')
output_file.close
print(test_ids)