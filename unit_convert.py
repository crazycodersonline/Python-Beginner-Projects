
units = ['mm' , 'cm' , 'm']
print("Choose for the following units:")
for unit in units:
    print(unit,end='\t')
print()

num = float(input("Enter the number: "))
unit1 = input("Which unit you want it converted from: ")
unit2 = input("Which unit you want it converted to: ")

if unit1 in units and unit2 in units:
    if unit1 == 'mm' and unit2 == 'cm':
        converted_num = num/10

    elif unit == 'mm' and unit2 == 'm':
        converted_num = num/1000
        
    elif unit1 == 'cm' and unit2 == 'mm':
        converted_num = num*10
        
    elif unit1 == 'cm' and unit2 == 'm':
        converted_num = num/100
        
    elif unit1 == 'm' and unit2 == 'mm':
        converted_num = num*1000
        
    elif unit1 == 'm' and unit2 == 'cm':
        converted_num = num*100
else:
    print("Unit not found")
      
print('Converted number:',converted_num, unit2) 
    
