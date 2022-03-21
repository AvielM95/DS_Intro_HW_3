# -*- coding: utf-8 -*-

##A
#"C:\\Users\\aviel\\Python\\Homework\\ex3_text.txt"





def read_line(n,file) :
    
        try:
            filename = open(file)
        except :
               return "file not found"
      
        x = filename.readlines() 
        if type(n) == int :
            if n> len(x) :
                return f"line {n} doesnt exist"

        else:
            return "invalid input detected"

        return x[n-1]
       
             
print(read_line(40, "C:\\Users\\aviel\\Python\\Homework\\ex3_text.txt"))
                          
    
                 




#%%
#B

lst = list()
lst2 = list()
final_lst = list()
def longest_words(file):
    try:
        filename = open(file)
    except :
           return "file not found" ,list()
           

    for i in filename:
        words = i.split()
        for word in words:
            if not word.startswith("-"):
                lst.append(word)  
    for j in lst:
        sep = j.split(".")
        for i in sep:
            i = i.rstrip(",")
            lst2.append(i)        
    sort= sorted(lst2,key = len,reverse=True)       
    final_lst = sort[:5]   
    return(final_lst)



print(longest_words("C:\\Users\\viel\\Python\\Homework\\ex3_text.txt"))











