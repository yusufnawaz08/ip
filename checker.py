def validate_ip(ip_address): 
     errors = []  
     part1,part2,part3,part4 = user_ip.split(".")  
     parts = [part1,part2,part3,part4]  
     print(parts) 
     parts = len(parts) 
     print(parts) 

  

  

    if parts != 4: 
         print("Invalid IP format: must contain 4 bytes separated by dots.") 
         return 

  

    labels = ["First", "Second", "Third", "Fourth"] 

  

    for i in len(parts) - 1: 
         part = parts[i]  
         try: 
             part = int(part)  
             if value < 0 or value > 255:  
                 errors = labels[i] + " Byte Invalid"  
         except: 
             errors = labels[i] + " Byte Invalid (not a number)"  
 
     print(errors)         
 
     if errors != 0: 
         for err in errors:  
             print(err)  
 
     else: 
         print("IP Valid") 

  

try: 
     ip_address = input("Enter an IPv4 address: ")  
     user_ip = ip_address  
     validate_ip(user_ip)  
except:  
     print("An error occured!") 