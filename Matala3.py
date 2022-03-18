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
           return "file not found"

    for i in filename:
        words = i.split()
        for word in words:
            if not word.startswith("-"):
                lst.append(word)  
    for j in lst:
        sep = j.split(".")
        for i in sep:
         lst2.append(i)
    x= sorted(lst2,key = len,reverse=True)       
    final_lst = x[:5]   
    return(final_lst)



print(longest_words("C:\\Users\\aviel\\Python\\Homework\\ex3_text.txt"))







