def clear_dublicat(apart_contact_list, counter, contacts_list):
      full_name_list = []
      connected_full_name_list = []

      for A in apart_contact_list:
        y = f'{A[0]} {A[1]}'
        connected_full_name_list.append(y)
        bv = [A[0], A[1]]
        full_name_list.append(bv)

      counter_4 = 0
      dict_fullname_keys = []

      for k in connected_full_name_list:
        result = {k: apart_contact_list[counter_4][2:]}
        counter_4 += 1
        dict_fullname_keys.append(result)

      dict_fullname = {}

      for contact in dict_fullname_keys:
        for key, values in contact.items():
          if key not in dict_fullname:
            dict_fullname.update({key: values})
          else:
            if values[0] not in dict_fullname[key][0] and values[0] == '' or dict_fullname[key][0] == '':
              dict_fullname[key][0] = values[0]
            if values[1] not in dict_fullname[key][1] and values[0] == '' or dict_fullname[key][1] == '':
              dict_fullname[key][1] = values[1]
            if values[2] not in dict_fullname[key][2] and values[0] == '' or dict_fullname[key][2] == '':
              dict_fullname[key][2] = values[2]
            if values[3] not in dict_fullname[key][3] and values[0] == '' or dict_fullname[key][3] == '':
              dict_fullname[key][3] = values[3]
            if values[4] not in dict_fullname[key][4] and values[0] == '' or dict_fullname[key][4] == '':
              dict_fullname[key][4] = values[4]

      counter_5 = 0
      full_contact_list = []

      for _ in range(counter -1):
          for k, v in dict_fullname.items():
            if k == f'{full_name_list[counter_5][0]} {full_name_list[counter_5][1]}':
              full_contact_list.append(full_name_list[counter_5] + v)
          counter_5 += 1


      clear_list = []

      for c in full_contact_list:
        if c not in clear_list:
          clear_list.append(c)

      upload_contact_list = [contacts_list[0]] + clear_list

      return  upload_contact_list