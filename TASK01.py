import sys
def sum_list(list):
    di={}
    end=0
    for i in range(len(list)):
        while(end<len(list)):
            key = tuple(list[i:end+1])
            di[key]=sum(list[i:end+1])
            end+=1
        end=0
    ends = len(list)-1
    for j in range(len(list)):
        start=j
        while(ends>start+1):
            list1=[]
            list1.append(list[start])
            list1.append(list[ends])
            di[tuple(list1)]=sum(list1)
            ends-=1
        ends=len(list)-1

    return di
    
lista = [1,2,3,4,5,6]
listb = [9,10,11,12,13,14]


possible_sum_a=sum_list(lista)
possible_sum_b=sum_list(listb)




for (b_key,b_val) in possible_sum_b.items() :
        for(a_key,a_val) in possible_sum_a.items():
            if a_val==b_val:
                print(a_key,b_key)
                sys.exit()
print(0)

            
        
            
            


    


    

