

      #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
     # # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
     ### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
     # # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
     # # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  
#Ahmed Demirezen Feezx1

import sys
import math

l = 4
h = 5
t = input("Lutfen cikti alinacak string i giriniz:\n")
l_ilk=l
harf_list=[" #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###","# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #","### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##","# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #      ","# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  # "]
harfler="ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
sozluk={}
test=[]
for i in range(len(harfler)):
    sozluk[harfler[i]]=(l-l_ilk,l)
    l=l+l_ilk
  
t=t.upper()

for k in range(h):
    for m in range(len(t)):
        if harfler.count(t[m])==1:
            print(harf_list[k][sozluk[t[m]][0]:sozluk[t[m]][1]],end="")
        else:
            print(harf_list[k][sozluk["?"][0]:sozluk["?"][1]],end="")
            
    print("")
                
