from art import *

tprint("-------------")
tprint("Magor Software")
tprint("                DECRYPTION")
tprint("-------------")


kulcsone =input() #("2, 3, 6")  
kulcstwo = input() #("7, 842") 
massege = input()#("918759") 

kulcstwo = [int(x) for x in kulcstwo.split(", ")]
kulcsone = [int(x) for x in kulcsone.split(", ")]
print(kulcstwo)
massege = int(massege) - int(kulcstwo[1])
massege = int(massege) // int(kulcstwo[0])

massege = list(str(massege))
print (massege)
