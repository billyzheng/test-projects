file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/defaults/main.yml', 'r')
count = 0
lines = file.readlines()
for line in lines:
    if 'Manage' in line:
        count += 1

print(f'Number of lines containing tasks: {count}')