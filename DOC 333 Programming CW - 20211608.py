#DOC333 Introduction to Programming - Coursework

#Initializing Variables

radius=0
height=0
length=0
width=0
area=0
volume=0
choice=0
again=0

#Menu & taking inputs

def menu():
    print("\nSHAPES CALCULATOR")
    print("\n1. Calculate Surface Area of a cone \n2. Calculate Volume of a cone \n3. Calculate Base area of a cone \n4. Calculate Volume of a rectangular pyramid \n5. Calculating Surface area of a rectangular pyramid \n6. Exit")
    choice=int(input("\nEnter Your Preferred Option : "))
    while choice<1 or choice>6:
        print("\nEnter one option number from above")
        choice=int(input("\nEnter Your Preferred Option : "))

    import math
    
#Calculating Surface area of cone - option 01
    
    if choice==1:
        radius=float(input("\nEnter radius of cone : "))
        while radius<0 or radius==0:
            print("\nRadius cannot be negative or equal to 0")
            radius=float(input("\nEnter radius of cone : "))
        length=float(input("\nEnter length of cone : "))
        while length<0 or length==0:
            print("\nLength cannot be negative or equal to 0")
            length=float(input("\nEnter length of cone : "))
        area=math.pi*(radius**2)+math.pi*radius*length
        print("\nSurface area of a cone : ",format(float(area),".2f"))
        again=input("\nDo you want to continue (Y/N) : ")
        if again=="Y" or again=="y":
            menu()
        else:
            exit()

#Calculating Volume of cone - option 02
            
    if choice==2:
        radius=float(input("\nEnter radius of cone : "))
        while radius<0 or radius==0:
            print("\nRadius cannot be negative or equal to 0")
            radius=float(input("\nEnter radius of cone : "))
        height=float(input("\nEnter height of cone : "))
        while height<0 or height==0:
            print("\nHeight cannot be negative or equal to 0")
            height=float(input("\nEnter height of cone : "))
        volume=1/3*math.pi*(radius**2)*height
        print("\nVolume of a cone : ",format(float(volume),".2f"))
        again=input("\nDo you want to continue (Y/N) : ")
        if again=="Y" or again=="y":
            menu()
        else:
            exit()

#Calculating Base area of cone - option 03
            
    if choice==3:
        radius=float(input("\nEnter radius of cone : "))
        while radius<0 or radius==0:
            print("\nRadius cannot be negative or equal to 0")
            radius=float(input("\nEnter radius of cone : "))
        area=math.pi*radius**2
        print("\nBase area of a cone : ",format(float(area),".2f"))
        again=input("\nDo you want to continue (Y/N) : ")
        if again=="Y" or again=="y":
            menu()
        else:
            exit()
            
#Calculating Volume of a rectangular pyramid - option 04
            
    if choice==4:
        length=float(input("\nEnter length of pyramid : "))
        while length<0 or length==0:
            print("\nLength cannot be negative or equal to 0")
            length=float(input("\nEnter length of pyramid : "))
        width=float(input("\nEnter wdith of pyramid : "))
        while width<0 or width==0:
            print("\nWidth cannot be negative or equal to 0")
            width=float(input("\nEnter width of pyramid : "))
        height=float(input("\nEnter height of cone : "))
        while height<0 or height==0:
            print("\nHeight cannot be negative or equal to 0")
            height=float(input("\nEnter height of pyramid : "))
        volume=length*width*height/3
        print("\nVolume of a rectangular pyramid : ",format(float(volume),".2f"))
        again=input("\nDo you want to continue (Y/N) : ")
        if again=="Y" or again=="y":
            menu()
        else:
            exit()
            
#Calculating Surface area of a rectangular pyramid - option 05
            
    if choice==5:
        length=float(input("\nEnter length of pyramid : "))
        while length<0 or length==0:
            print("\nLength cannot be negative or equal to 0")
            length=float(input("\nEnter length of pyramid : "))
        width=int(input("\nEnter wdith of pyramid : "))
        while width<0 or width==0:
            print("\nWidth cannot be negative or equal to 0")
            width=float(input("\nEnter width of pyramid : "))
        height=float(input("\nEnter height of pyramid : "))
        while height<0 or height==0:
            print("\nHeight cannot be negative or equal to 0")
            height=float(input("\nEnter height of pyramid : "))
        area=length*width+(length*math.sqrt((width/2)**2+height**2))+(width*math.sqrt((length/2)**2+height**2))
        print("\nSurface area of a rectangular pyramid : ",format(float(area),".2f"))
        again=input("\nDo you want to continue (Y/N) : ")
        if again=="Y" or again=="y":
            menu()
        else:
            exit()
        
            
#Exiting the programme

    if choice==6:
        exit()
        

    
menu()






            
    
