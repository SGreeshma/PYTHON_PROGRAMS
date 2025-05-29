# COMBINATION SUM
def generate(ind, curr, ans, cand, target):
    if (target==0):
        ans.append(curr.copy())
        return
    if(target <0 or ind==len(cand)):
        return
    curr.append(cand[ind])
    generate(ind, curr, ans, cand, target-cand[ind])
    curr.pop()
    generate(ind+1, curr, ans, cand, target)
def comSum(cand, target):
    ind=0
    curr=[]
    ans=[]
    generate(ind, curr, ans, cand, target)
    return ans
cand=[2, 3, 6, 7]
target=7
print(comSum(cand, target))