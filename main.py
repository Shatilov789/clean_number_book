from contact_list import clear
from number import clear_number
from delete_dublicat import clear_dublicat
import csv
if __name__ == '__main__':
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    counter = len(contacts_list)

    apart_contact_list = clear(counter,contacts_list)
    apart_contact_list = clear_number(apart_contact_list)
    upload_contact_list = clear_dublicat(apart_contact_list, counter,contacts_list)

  with open("phonebook.csv", "w", encoding= 'utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(upload_contact_list)
