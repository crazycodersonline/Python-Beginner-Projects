A = ['c' , 'o' , 'm' , 'p' , 'u' , 't' , 'e' , 'r']
L = ['_' , '_' , '_', '_' , '_' , '_' ,'_' ,'_'  ]

attemps_remaining = 6

while attemps_remaining > 0:
    letter = input(f"Guess a letter ({attemps_remaining}) : ")
    
    if letter not in A:
        attemps_remaining -= 1
        
    else:
        i = 0
        for currentletter in A:
            if letter == currentletter :
                L[i] = letter
            i += 1
            
    print(' '.join(L))
    
    if L == A:
        print("You won")
        break
else:
    print("You lost")