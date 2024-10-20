from MN import BigNumber as bn 

list_nums = [
    bn(1,1),
    bn(2,1),
    bn(1,2),
    bn(2,2),

    bn(-1,1),
    bn(-2,1),
    bn(-1,2),
    bn(-2,2),

    bn(1,-1),
    bn(2,-1),
    bn(1,-2),
    bn(2,-2),

    bn(-1,-1),
    bn(-2,-1),
    bn(-1,-2),
    bn(-2,-2),
]

string = "||||||"
for x in list_nums:
    string += str(x) 
print(string)
n = 0
for num in list_nums:
    n+=1
