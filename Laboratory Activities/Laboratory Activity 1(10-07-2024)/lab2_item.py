char1,char2= (input("Enter two-seperated space characters: ")).split()
asciiVal1 = ord(char1)
asciiVal2 = ord(char2)

print("--------------------------")
greatValue=max(char1,char2)
print("The caharacter with greater value is: " + greatValue)
print("--------------------------")

print("This part is optional to include.")
print('Showing ASCII Values:'+f'\n{char1}: {asciiVal1}\n{char2}: {asciiVal2} ')