# -*- coding: utf-8 -*-
from Role import SwordsMan,Adviser,Dancer

import random

if __name__=='__main__':
    
    player=list()
    com=list()
    
    for i in range(3):
        p=int(input('劍士請按1,軍師請按2,舞者請按3'))
        
        name=input('請輸入角色姓名:')
        
        if p==1:
            player.append(SwordsMan(name, 100, 60))

        elif p==2:
            player.append(Adviser(name,100,120))
            
        else:
            player.append(Dancer(name,100,80))
            
        
        
    for i in range(3):
        c=random.randint(1,3)
        name=['魯夫','索隆','娜美','騙人布','香吉士','羅賓','喬巴']
            
        if c==1:
            com.append(SwordsMan(random.choice(name),100,60))
                
        elif p==2:
            com.append(Adviser(random.choice(name),100,120))
                
        else:
            com.append(Dancer(random.choice(name),100,80))
                
    while len(player)>0 and len(com)>0:
            
        n=random.randint(1,100)
            
        if n%2==0:
                
            print(player[0].getName(),'使出:',end='')
            if random.randint(1,10)==3:
                player[0].skill()
                boold=random.randint(15,30)
                   
            else:
                player[0].fight()
                blood=random.randint(5,10)
                    
                com[0].setHp(com[0].getHp()-blood)
                          
                print(com[0].getName(),'的血量剩:',com[0].getHp())   
            if com[0].getHp()<0:
                pop=com.pop(0)
                        
                                      
        else:
                    
            print(com[0].getName(),'使出:',end='')
            if random.randint(1,10)==3:
                com[0].skill()
                boold=random.randint(15,30)
                        
            else:
                com[0].fight()
                boold=random.randint(5,10)
                        
                player[0].setHp(player[0].getHp()-boold)
                        
                print(player[0].getName(),'的血量剩:',player[0].getHp())
                    
            if player[0].getHp()<0:
                pop=player.pop(0)
                        
           
    if len(player)>len(com):
        print('玩家勝利')
            
    else:
        print('電腦勝利')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                          
            