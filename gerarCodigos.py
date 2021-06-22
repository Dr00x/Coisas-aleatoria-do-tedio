def GenerateCode(bool_value,time,done_value):
    from colorama import init , Fore
    from random import randint
    from time import sleep

    init(convert=True,autoreset=True)
    c = 0
    words = ["  {","}","  function(1313@4+TrueType){ [[  ]  chapter[i]+=","{"," }","[[ chap ]] && chapter[$i]+=","-0gMakefile","__init__","    Makefile","Makefile","USE_L10N = True","USE_L10N = True","' django.contrib.staticfiles.finders.FileSystemFinder',"," int main(){","char c;","c   =getch();","        }while(c!=(char)13);","         if(a==3)b=3;else b=4;","    int ms,es,mts,ches,phys;","default: printf(error); break;","return 0;","switch(ans","float fArea,fRadius;","for(x=1;x<=10;x++)","a=3.14*r*r;","     {","    }","{","}","float funArea(float r)","return a;"]
    while bool_value and c <= time:
        c = c+1
        a = randint(0,20)
        n = print(Fore.GREEN + f"{words[randint(1,22)]}" , end='\n')
        n
        if a <=7:
            print(f"    ")
            # print(Fore.RED + f"{words[randint(1,22)]}" , end='\n')
            # print(Fore.BLUE + f"{words[randint(1,22)]}" , end='\n')
            # print(Fore.YELLOW + f"{words[randint(1,22)]}" , end='\n')
        
        if c - 1 >= time:
            print(done_value)
        sleep(0.1)
    
a = input("Coloque os valores\n>:")
print("Calculando...")
GenerateCode(True,50,"Completo")