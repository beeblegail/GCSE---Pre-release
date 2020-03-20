# International General Certificate of Secondary Education - Pre Release Material 2020 - Task 3
# Author : Abigail Pates
# Date : 26.02.2020
# Version : 0.1

Category = ["Phone","Phone","Phone","Phone","Phone","Phone","Tablet","Tablet","Tablet","Tablet","Sim Card","Sim Card","Case","Case","Charger","Charger","Charger"]
Item_Code = ["BPCM","BPSH","RPSS","RPLL","YPLS","YPLL","RTMS","RTLM","YTLM","YTLL","SMNO","SMPG","CSST","CSLX","CGCR","CGHM","CGBT"]
Description = ["Compact","Clam Shell","RoboPhone - 5-inch screen and 64GB memory","RoboPhone - 6-inch screen and 256GB memory","Y-Phone Standard - 6-inch screen and 64GB memory","Y-Phone Deluxe - 6-inch screen and 256GB memory","RoboTab - 8-inch screen and 64GB memory","RoboTab - 10-inch screen and 128GB memory","Y-Tab Standard - 10-inch screen and 128GB memory","Y-Tab Deluxe - 10-inch screen and 256 memory","Sim Free (no sim card purchased)","Pay As You Go (Sim card purchased)","Standard","Luxury","Car","Home","Both"]
Price = ["29.99","49.99","199.99","499.99","549.99","649.99","149.99","299.99","499.99","599.99","0.00","9.99","0.00","50.00","19.99","15.99","35.98"]


def check_input(choices) :
    choice = input("Enter a number (1-"+str(choices)+") to choose: ")
    checked = 0
    chose = int(choice)
    while checked != 1:
        for i in range (1,choices+1):
            if chose == i:
                checked = 1
    return(chose)
    
if __name__ == '__main__':
    final_total = 0
    choices = 1
    total = 0
    for counter in range(len(Category)):
        if Category[counter] == "Phone" or Category[counter] == "Tablet":
            print(choices, Description[counter], " - ", Price[counter])
            choices += 1
    choices -= 1
    print("Devices")
    chose = check_input(choices)
    chose -= 1
    print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
    total += float( Price[chose] )
    choices = 1
    print(total)
    
    for counter in range(len(Category)):
        if Category[counter] == "Sim Card":
            print(choices, Description[counter], " - ", Price[counter])
            choices += 1
    choices -= 1
    print("Sim Cards")
    chose = check_input(choices)
    chose += 9
    print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
    total += float( Price[chose] )
    choices = 1
    print(total)

    case = input("Would you like a case? ")
    if  case == "yes" or case == "y":
        for counter in range(len(Category)):
            if Category[counter] == "Case":
                print(choices, Description[counter], " - ", Price[counter])
                choices += 1
        choices -= 1
        print("Cases")
        chose = check_input(choices)
        chose += 11
        print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
        total += float( Price[chose] )
        choices = 1        
    charger = input("Would you like a charger? ")
    if charger == "yes" or charger == "y":
        for counter in range(len(Category)):
            if Category[counter] == "Charger":
                print(choices, Description[counter], " - ", Price[counter])
                choices += 1
        choices -= 1
        print("Chargers")
        chose = check_input(choices)
        chose += 13
        print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
        total += float( Price[chose] )
        choices = 1        
        
        print("The cost of this device is: $" , round(total,2))
        final_total += total 
        device = input("Would you like another device? ")
        
    while device == "yes" or device == "y":
        choices = 1
        total = 0
        for counter in range(len(Category)):
            if Category[counter] == "Phone" or Category[counter] == "Tablet":
                print(choices, Description[counter], " - ", Price[counter])
                choices += 1
        choices -= 1
        print("Devices")
        chose = check_input(choices)
        chose -= 1
        print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
        total += (float( Price[chose] ) * 0.9)
        choices = 1
	
        for counter in range(len(Category)):
            if Category[counter] == "Sim Card":
                print(choices, Description[counter], " - ", Price[counter])
                choices += 1
        choices -= 1
        print("Sim Cards")
        chose = check_input(choices)
        chose += 9
        print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
        total += float( Price[chose] )
        choices = 1

        case = input("Would you like a case? ")
        if  case == "yes" or case == "y":
            for counter in range(len(Category)):
                if Category[counter] == "Case":
                    print(choices, Description[counter], " - ", Price[counter])
                    choices += 1
            choices -= 1
            print("Cases")
            chose = check_input(choices)
            chose += 11
            print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
            total += float( Price[chose] )
            choices = 1
		
        charger = input("Would you like a charger? ")
        if charger == "yes" or charger == "y":
            for counter in range(len(Category)):
                if Category[counter] == "Charger":
                    print(choices, Description[counter], " - ", Price[counter])
                    choices += 1
            choices -= 1
            print("Chargers")
            chose = check_input(choices)
            chose += 13
            print(Category[chose] + " - " + Item_Code[chose] + "  - " + Description[chose] + " - " + Price[chose] + "\n")
            total += float( Price[chose] )
            choices = 1
	
        

        print("The cost of this device is: $" , round(total,2))
        final_total += total 
        device = input("Would you like another device? ")


print("The final total is: " , round(final_total,2))
