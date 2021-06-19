
def clear(counter, contacts_list):

    new_contacts_list1 = []
    full_name_apart = []
    counter_2 = 1

    for _ in range(counter -1):
        join_name_person = [' '.join(contacts_list[counter_2][0:2])]
        split_name_person = join_name_person[0].split()
        new_contacts_list1.append(contacts_list[counter_2][3:])
        full_name_apart.append(split_name_person)
        counter_2 += 1

    for full_name in full_name_apart:
        full_name.append('')
    full_name_apart.append(full_name)

    counter_3 = 0
    apart_contact_list = []

    for _ in range(counter - 1):
        apart_contact_list.append(full_name_apart[counter_3][:3] + new_contacts_list1[counter_3][:4])
        counter_3 += 1
    return apart_contact_list