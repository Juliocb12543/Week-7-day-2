def enum():
  # enumerate
  print("enumerate")
  # enumerate is a very useful function to use with for loops. Let's imagine the following 
  my_list = ['a', 'b', 'c']
  print(my_list)
  for index, item in enumerate(range(0,50)):
    print(index, item)

  
  ##############################enumerators in python #####################################################
  
  
  # Enumerator Practice #1
  # Print sentences like the following on the screen:
  
  # '{name} is found at index {index}'
  
  # Where name must be each of the names in the list below, and the index, must be obtained via enumerate().
  
  # list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
  
  # You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!
  
  # Tip: use loops!
  
  # list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
  
  # print(f'{nombre} se encuentra en el índice {indice}')
  
  
  
  # Enumerator Practice #2
  # Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.
  
  # Call the returned list with the variable name indices_list.
  
  # "Python"
  
  
  # Enumerator Practice #3
  # Print to the screen only the indices of those names in the list below, that start with M:
  
  # list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
  
  # You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:
  
  # loops
  
  # if conditionals
  
  # the enumerate() method
  
  # string methods and indexing
  
  # list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
  
