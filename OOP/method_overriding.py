class Father:

    def vote(self):
        print("Vote for ABC party")

class Son(Father):

    def vote(self):
        print("Vote for XYZ party")

obj = Son()
print(obj.vote())