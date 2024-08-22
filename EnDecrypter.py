print('Welcome to EnDecrypter!')
print('\nSelect what you desire: ')
print('\nEncryption:       Type 0')
print('Decryption:       Type 1')

user_input = int(input('Type here: '))

def encrypter():
        
    a = input('Enter here: ')

    b = list(a)
    
    if len(b) > 3:
    
        first_item = b[0]
    
        b.append(first_item)
        b.pop(0)
    
        a = ''.join(b)
        
        import random 
        import string
    
        alpha1 = [random.choice(string.ascii_letters) for _ in range(3)]
    
        list_to_string1 = ''.join(alpha1)
        
        alpha2 = [random.choice(string.ascii_letters) for _ in range(3)]
    
        list_to_string2 = ''.join(alpha2)
     
        print(list_to_string1+a+list_to_string2)
        
    else:
        
        b.reverse()
        
        a = ''.join(b)
        
        print(a)
        
def decrypter():
    
    str_user = input('Enter here: ')

    list_user = list(str_user)
    
    if len(list_user) > 3:
        
        for i in range(3):
            
            list_user.pop(0)
            
            list_user.pop(len(list_user)-1) 
    
        extract = list_user[len(list_user)-1]
    
        list_user.pop(len(list_user)-1)
    
        final = ''.join(list_user)
        extract_final = ''.join(extract)
        
        print(extract_final + final)
        
    else:
        
        list_user.reverse()
        
        final = ''.join(list_user)
        
        print(final)

def main():
    
    match user_input :
        
        case 0:
            encrypter()
        
        case 1:
            decrypter()
main() 