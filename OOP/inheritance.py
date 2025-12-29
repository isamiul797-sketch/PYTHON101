# #SINGLE INHERITANCE
# class Father: #parent class

#     x = 10
#     y = 20

#     def add(self):
#         print(self.x + self.y)

# class Son(Father):  #child class
#     a = 30
#     b = 20

#     def sub(self):
#         print(self.a - self.b)

# obj = Son()

# #Inheritance
# print(obj.x)
# print(obj.y)
# print(obj.add())

# #self
# print(obj.a)
# print(obj.b)
# print(obj.sub())



#MULTIPLE INHERITANCE

# class Father: #parent class

#     x = 10
#     y = 20

#     def add(self):
#         print(self.x + self.y)

# class Mother:  # parent class
#      g = 20
#      h = 90

#      def mul(self):
#          print(self.g * self.h)

# class Son(Father,Mother):  # child class
#     a = 30
#     b = 20

#     def sub(self):
#         print(self.a - self.b)


# obj = Son()
# #Inheritance
# print(obj.x)
# print(obj.y)
# print(obj.add())

# print(obj.g)
# print(obj.h)
# print(obj.mul())

# #self
# print(obj.a)
# print(obj.b)
# print(obj.sub())


#MULTILEVEL INHERITANCE

# class Father: #parent class

#     x = 10
#     y = 20

#     def add(self):
#         print(self.x + self.y)

# class Mother(Father):  # child class
#      g = 20
#      h = 90

#      def mul(self):
#          print(self.g * self.h)

# class Son(Mother):  # child class
#     a = 30
#     b = 20

#     def sub(self):
#         print(self.a - self.b)


# obj = Son()
# #Inheritance
# print(obj.x)
# print(obj.y)
# print(obj.add())

# print(obj.g)
# print(obj.h)
# print(obj.mul())

# #self
# print(obj.a)
# print(obj.b)
# print(obj.sub())