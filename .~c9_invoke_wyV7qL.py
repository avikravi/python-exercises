#Exercise 1 
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
print(phonebook_dict)