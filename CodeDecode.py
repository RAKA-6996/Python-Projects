import random

usinp = input("Enter a message: ")

words = usinp.split(" ")


options = int(input("Select 1 for Encryption 0 for Decryption: "))

def main():
    if options ==1:
            neword = []
            for word in words:
                if len(word) >= 3:
                    r1 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
                    r2 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
                    
                    x = r1 + word[1:] + word[0] + r2
                    neword.append(x)
                else:
                    neword.append(word[::-1])
            print(" ".join(neword))
            
    elif options==0:
            neword = []
            for word in words:
                if len(word) >= 3:
                    
                    x = word[3 : -3]
                    x = x[-1] + x[:-1]
                    neword.append(x)
                else:
                    neword.append(word[::-1])
            print(" ".join(neword))    
            
    else:
        raise ValueError ("Invalid input! Select from the given options.")
main()