class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        arr = [] #set up an array to store values
        f = False #used like sign to tell whether the integer is negative or not
        if x<0:
            x=-x
            f=True
        while True:
            arr.append(x%10) #get the number of each poisition
            x=x/10
            if x==0:
                break
        result = 0
        for i in arr: #restor the reverse integer
            result = i+10*result
        if f: #restore the negative num.
            result *= -1
        return result
