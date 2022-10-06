class ArithmeticProgression():

    def get(self,n,a,d):
        curr_term=0

        for i in range(1,n+1):
            curr_term=a+(i-1)*d

        return curr_term

    def sum(self,n,a,d):

        s = (n * (2 * a + (n - 1) * d)) / 2

        return s

