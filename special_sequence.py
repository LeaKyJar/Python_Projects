def sumOfTheDigits(q):
    # Write your code here
    #create array of patterns first
    pattern = ["1"]
    highest_query = max(q)
    for i in range(highest_query):
        ans = ""
        temp = list(pattern[i])
        flag = False
        for j in range(len(temp)):
            if temp[j] == "1" and not flag and j!=len(temp)-1:
                if temp[j+1] == "1": #checks if next integer is 1
                    flag = True
                    ans += "21"
                else:
                    ans += "11"
            elif temp[j] == "1" and not flag and j==len(temp)-1:
                ans += "11"
            elif temp[j] == "1" and flag:
                flag = False
            elif temp[j] == "2":
                flag = False
                ans += "12"
        pattern.append(ans)
    q = q[1:]
    print(q)
    ls = []
    for i in q:
        counter = 0
        for j in pattern[i-1]:
            counter+=int(j)
        ls.append(counter)
    return ls

print(sumOfTheDigits([40,1,2,32]))
