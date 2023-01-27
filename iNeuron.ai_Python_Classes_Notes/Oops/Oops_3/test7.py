class ineuron:
    __students = "data science"
    public_variable = "ML"

    def class_method(self):
        print(ineuron.__students)

    def object_method(self):
        print(self.__students)

    def class_method_pub(self):
        print(ineuron.public_variable)

    def obj_method_pub(self):
        print(self.public_variable)


i = ineuron()
#print(i.class_method())
# print(i.object_method())
# print(i.class_method_pub())
# print(i.obj_method_pub())

print(ineuron.class_method(i))
