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
            count = 0
            for i in x :
                count+=1
            if n>count :
                return "line", n ,"doesnt exist"
                           
        
        if type(n) == str:
            return "invalid input detected"

        else:
            return x[n-1]
       
             
print(read_line(4, "C:\\Users\\aviel\\Python\\Homework\\ex3_text.txt"))
                          
    
                 




#%%
#B

lst = list()
final_lst = list()
def longest_words(file):
    try:
        filename = open(file)
    except :
           return "file not found"

    for i in filename:
        words = (i.split())
        for word in words:
            lst.append(word)
    x= sorted(lst,key = len,reverse=True)       
    final_lst = x[:5]   
    return(final_lst)



print(longest_words("C:\\Users\\aviel\\Python\\Homework\\ex3_text.txt"))






