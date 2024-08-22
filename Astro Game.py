print('Welcome to Game of Astrology!')
print()
print('Follow the below options as per your choice:')
print()

t = "PRESS"
s = [0,1,2,3,4]  # List for accessing details
r = ""

print('DETAILS', t.center(50))
print('What is Astrology?', r.center(12), s.index(0))
print('History of Astrology', r.center(10), s.index(1))
print('Zodiac Signs by Month', r.center(9), s.index(2))
print('Zodiac Elements', r.center(15), s.index(3))
print('Detailed Zodiac Signs', r.center(9), s.index(4))

print()

x = int(input("Enter your desired option: "))

# Dictionary for accessing Zodiac signs 
y = {1:'Aries', 2:'Taurus', 3:'Gemini',
     4:'Cancer', 5:'Leo', 6:'Virgo',
     7:'Libra', 8:'Scorpio', 9:'Sagittarius',
     10:'Capricon', 11:'Aquarius', 12:'Pisces'}

# Dictionary for accessing Elements
w = {1:'Fire', 2:'Earth', 3:'Air', 4:'Water'}

k = y.copy()  # duplicate copy of y as k for case 4

list_1 = ['Symbol: The Ram',
           'Element: Fire',
           'Quality: Cardinal',
           'Ruling Planet: Mars',
           'Traits: original, assertive, bold, passionate, impulsive']

list_2 = ['Symbol: The Bull',
          'Element: Earth',
          'Quality: Fixed',
          'Ruling Planet: Venus',
          'Traits: determined, practical, creative, stubborn']

list_3 = ['Symbol: The Twins',
          'Element: Air',
          'Quality: Mutable',
          'Ruling Planet: Mercury',
          'Traits: intellectual, adaptable, curious, flighty']

list_4 = ['Symbol: The Crab',
          'Element: Water',
          'Quality: Cardinal',
          'Ruling Planet: The Moon',
          'Traits: sensitive, persistent, domestic, caring']

list_5 = ['Symbol: The Lion',
          'Element: Fire',
          'Quality: Fixed',
          'Ruling Planet: The Sun',
          'Traits: generous, noble, powerful, proud']

list_6 = ['Symbol: The Virgin',
          'Element: Earth',
          'Quality: Mutable',
          'Ruling Planet: Mercury',
          'Traits: pragmatic, analytical, reliable, critical']

list_7 = ['Symbol: The Scales',
          'Element: Air',
          'Quality: Cardinal',
          'Ruling Planet: Venus',
          'Traits: fair, balanced, romantic, passive-aggresive']

list_8 = ['Symbol: The Scorpion',
          'Element: Water',
          'Quality: Fixed',
          'Ruling Planets: Mars, Pluto',
          'Traits: mysterious, secretive, intense, deep']

list_9 = ['Symbol: The Archer',
          'Element: Fire',
          'Quality: Mutable',
          'Ruling Planet: Jupiter',
          'Traits: honest, adventurous, loves freedom, blunt']

list_10 = ['Symbol: The Mountain Goat',
          'Element: Earth',
          'Quality: Cardinal',
          'Ruling Planet: Saturn',
          'Traits: ambitious, responsible, organized, selfish']

list_11 = ['Symbol: The Water Bearer',
          'Element: Air',
          'Quality: Fixed',
          'Ruling Planets: Saturn, Uranus',
          'Traits: tolerant, idealistic, independent, aloof']

list_12 = ['Symbol: The Fish',
          'Element: Water',
          'Quality: Mutable',
          'Ruling Planets: Jupiter, Neptune',
          'Traits: compassionate, creative, empathic, escapist']


list_main = [list_1, 
             list_2,
             list_3,
             list_4,
             list_5,
             list_6,
             list_7,
             list_8,
             list_9,
             list_10,
             list_11,
             list_12]    # main list with sublists for case 4

print()

# function for operating case 4: detailed zodiac sign
def case_4():
    
    print('Select your Zodiac Sign: ')
    
    print()
    
    for l, m in k.items():
        print(f'Press {l} for {m}.')
    print()
    
    switch = int(input('Enter here: '))
    
    print()
    
    match switch:
        
        case 1:
            print(list_main[0])
        
        case 2:
            print(list_main[1])
        
        case 3:
            print(list_main[2])
        
        case 4:
            print(list_main[3])
            
        case 5:
            print(list_main[4])
            
        case 6:
            print(list_main[5])
            
        case 7:
            print(list_main[6])
            
        case 8:
            print(list_main[7])
            
        case 9:
            print(list_main[8])
            
        case 10:
            print(list_main[9])
            
        case 11:
            print(list_main[10])
            
        case 12:
            print(list_main[11])
            
    return
# function for operating case3: zodiac Elements

def case_3():
    
    w = int(input('Enter here: '))
    
    print()
    
    match w:
        
        case 1:
            print('Aries, Leo, Sagittarius')
        
        case 2:
            print('Taurus, Virgo, Capricon')
            
        case 3:
            print('Gemini, Libra, Aquarius')
            
        case 4:
            print('Cancer, Scorpio, Pisces')
    
    return

# function for operating case2: zodiac signs by month
def case_2():
    
    z = int(input('Enter here: '))
    
    print()
    
    match z:
        
        case 1:
            print('March 19-April 19')
        case 2:
            print('April 20-May 19')
        case 3:
            print('May 20-June 19')
        case 4:
            print('June 20-July 21')
        case 5:
            print('July 22-August 21')
        case 6:
            print('August 22-September 21')
        case 7:
            print('September 22-October 21')
        case 8:
            print('October 22-November 20')
        case 9:
            print('November 21-December 20')
        case 10:
            print('December 21-January 18')
        case 11:
            print('January 19-February 17')
        case 12:
            print('February 18-March 19')
        
    return

# main function to operate the whole code and all other functions are called here.
def main():
    
    match x:   # switch cases for accessing details
        
        case 0:           
            print("""While astronomy is the core of the Almanac (which means “calendar of the heavens”), early Almanac readers were also very familiar with 'The Man of Signs,' which is astrology.\
                  Astrology is about so much more than simple horoscopes. It’s an ancient study with a rich history that focuses on how the stars and planets affect our lives on Earth.\
                  Astrologers believe the celestial bodies can dictate our personalities, life paths, and day-to-day events. While an element of fate is involved, modern astrologers believe you have free will and can work with the energy rather than assume you’re fated to one destiny based on your birth chart.""")
                  
            print()  
            
        case 1:
            print("""Astrology is a profound practice that has intrigued and captivated people for centuries. Imagine the awe of our ancestors as they learned to stand upright, communicate, and become fascinated with the night sky.\
                  They began to notice planets, eclipses, patterns, movements, and more. Soon, they learned how to use the energy of the moon for planting, fishing, and daily living.\
                  In time, this led to the development of a philosophy that became known as astrology.""")
                  
            print() 
            
        case 2:
            print('To know the detail of Dates of Zodiac Signs, follow instruction.')
            print()
            
            for i1, i2 in y.items():
                print(f"Press {i1} for {i2}")
                
            print()
            
            case_2()     # function for case 2 is called
            
        case 3:
            print('There are four elements in astrology: fire, earth, air, and water.')
            print('The zodiac signs are divided into groups of three signs belonging to the same element.')
            print('To know which element contains which zodiac sign, follow instructions.')  
            
            print()
            
            for w1, w2 in w.items():
                  print(f"Enter {w1} for {w2} element.")
            
            print()
            
            case_3()       # function for case 3 is called
            
        case 4:
            case_4()
main()