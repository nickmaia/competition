N = int(input()) # Get the number of test cases

for i in range(N): # Loop through the test cases
    s1, s2 = input().split() # Get two input strings and split them
    
    resposta = "" # Initialize an empty string to store the result
    try:
        for l1, l2 in zip(s1,s2): # Loop through the characters of both strings
            resposta += l1 + l2 # Concatenate the characters and add them to the result string
            
        if len(s1) == len(s2):
            print(resposta) # If both strings have the same length, print the result
    
        elif len(s2) > len(s1):
            tam = len(s1) - len(s2)
            ultima_letra = s2[tam:]
            print(resposta+ultima_letra) # If the second string is longer, add the remaining characters to the result string
        else:
            tam = len(s2) - len(s1)
            ultima_letra = s1[tam:]
            print(resposta+ultima_letra) # If the first string is longer, add the remaining characters to the result string
            
    except:
        break # If an exception occurs, exit the loop
