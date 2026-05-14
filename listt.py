# list - [](square bracket)
# can have duplicate values
#an have multiple data types
# list have a unique thing called indexing
#indexing starts with 0 and goes to len 1

# age = [] empty list 
# #    0    1   2
# age = [21, 22, 23] 
# print(age[2])



# 1 =[1,2,3,4,5,6,7]
# 1[3] =10 
# print(1)
          

#slicing 
# start_index:s_index:step_skip
# step(by_default = +1)

# #    0 1 2 3 4 5
# 1 = [1,2,3,4,5,6]
# print (1[1 : 4 :])

# l = [1,2,3,4,5]
# # for i in l :
# #     print(i)

# #index loop
# for i in range(len(l)):
#     print(i, l[i])



#METHODS IN LIST
# 1. append()
# 2. extent()
# 3. insert
# 4. pop()
# 5. remove()
# 6. clear()


# l = [1,2,3,4,5]
# l.append(6)
# print(l)


# l = [ 1,2,3,4,5]
# l1 = [6,7,8]
# # print(1 + l1)
# l.extend(l1)
# print(l)


# l = [ 1,2,3,4,5]
# l.insert(2,100)
# print(l)


# l = [ 1,2,3,4,5]
# l.pop(2)
# print(l)


# # l = [1,2,3,4,5]
# l.remove(5)
# print(l)


# l = [1,2,3,4,5]
# l.clear()
# print(l)


#rotate a list by k elements.

# l = [10,20,30,40,50]
# k = 2
# for i in range(k):
#     last = l[len(l)-1]
#     for j in range(len(l)-1,0,-1):
#         l[j] = l[j-1]
#     l[0] = last
# print(l)




#  FUMTION --------------------------------------------------------------------------------------------------------------
#def (define)
# def greet(gender:str):  # parameter
#     print(f"hello {gender}")
# greet('female')  # arguments



# rotate a list by k elements.








def rotate_elements(l,k):

        for i in range(k):
            last = l[len(l)-1]
            for j in range(len(l)-1,0,-1):
                l[j] = l[j-1]
            l[0] = last
        return l 
l = [10,20,30,40,50]
k = 2
rotate_elements(l,k)
print(rotate_elements(l,k))



