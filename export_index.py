import os
from prettytable import PrettyTable

file = open('/Users/ronechen/Ansible/test-projects/baselines/win_baseline/tasks/main.yml')
lines = file.readlines()

control_ids = []
table_data = []

for line in lines:
    if '- name: "win_baseline_' in line:
        control_id = line.split('_')[2].strip()
        control_ids.append(int(control_id))
    

control_ids = set(control_ids)
# print(f'items implemented and can run: {len(control_ids)}')
table_data.append(['items implemented and can run', len(control_ids)])
file.close()

manual_add = [2385, 2388, 2396, 2398, 2341, 2343, 2586, 3377, 3928, 4470, 4493, 4491, 1115, 1181, 2182, 2184, 19336, 11507]
# print(f'items implemented but cannot run: {len(manual_add)}')
table_data.append(['items implemented but cannot run', len(manual_add)])
control_ids = control_ids.union(manual_add)

# print(f'current finished tasks: {len(control_ids)}')
table_data.append(['current finished tasks', len(control_ids)])
# control_ids.sort()

file.close()

file = open('/Users/ronechen/Ansible/test-projects/control_ids.txt')
lines = file.readlines()
lines = lines[0].split(',')
exported_control_ids = [int(x.strip()) for x in lines]
exported_control_ids_len = len(exported_control_ids)
# print(f'all items in the baseline: {len(exported_control_ids)}')
table_data.append(['all items in the baseline', len(exported_control_ids)])
for id in control_ids:
    try:
        exported_control_ids.remove(id)
    except:
        pass
# print(f'finish rate: {100 - (len(exported_control_ids) / exported_control_ids_len) * 100:.4f}%')
table_data.append(['finish rate', f'{100 - (len(exported_control_ids) / exported_control_ids_len) * 100:.4f}%'])


table = PrettyTable()

table.field_names = ['Item', 'Value']
for row in table_data:
    table.add_row(row)

print(table)
# print(f'lefted items: {len(exported_control_ids)}')
fail_item = manual_add
# print(fail_item)
# print(exported_control_ids)
fail_set = manual_add + exported_control_ids
fail_set.sort()
for i, item in enumerate(fail_set):
    print(i,item)


print(f'\n4193 contains 5 different tasks.')
