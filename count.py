import time

for i in range(100000):
    file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/defaults/main.yml', 'r')
    count_1 = 0
    count_2 = 0
    lines = file.readlines()
    for line in lines:
        if 'Manage' in line:
            count_1 += 1
        if 'True' in line:
            count_2 += 1

    print(f'Number of lines containing tasks: {count_1, count_2}')
    file.close()
    time.sleep(60)
