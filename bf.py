import time
import colorama 

CRED = '\033[91m'
CEND = '\033[0m'
CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'
bf = input("Enter a day :")

if bf == "mon":
 print(CRED +"CHAPATHI" + CEND)

if bf == "tue":
 print(CGREEN2  +"DOSA" + CEND)

if bf == "wed":
 print(CWHITE2 +"PURI" + CEND)

if bf == "thur":
 print(CVIOLETBG2 +"IDLY"+ CEND)

if bf == "fri":
print(CYELLOW2 + "UTHAMPA"+ CEND)

if bf == "sat":
 print(CYELLOW2 + "UPMA"+ CEND)

else:
 print("day typed wrongly")
