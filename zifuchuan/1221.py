# 答案错误
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        if len(s)<=1:
            return 0
        last = None
        flag = True # begin
        change = False
        count = 0
        show = []
        for i in s:
            if last == None:
                change = False
                last = i
                count = 1
                flag = False
                show.append(i)
                continue

            if not flag and count !=0:
                if i==last and not change:
                    count += 1
                    show.append(i)
                elif i==last and change:
                    count -= 1
                    show.append(i)
                elif i!=last and not change:
                    change = True
                    count -= 1
                    last = i
                    show.append(i)
                else:
                    flag = True
            elif not flag and count==0:
                flag = True


            if flag:
                change = False
                last = i
                count = 1
                flag = False
                show.append(i)



            if count == 0:
                result += 1
                print(show)
                show = []
                #show.append(i)


        return result

# simple
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        pnum = 0
        lnum = 0
        res = 0
        for i in s:
            if i=='L':
                lnum+=1
            else:
                pnum += 1
            if pnum == lnum:
                res+=1
        return res

# stack
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if stack == []:
                stack.append(i)
            elif i == stack[-1]:
                stack.append(i)
            else:
                stack.pop(-1)
            if stack == []:
                res += 1
        return res
s = Solution()
print(s.balancedStringSplit("RLLLLRRRLR"))