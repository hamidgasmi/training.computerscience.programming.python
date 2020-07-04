class MyClass():

    def __init__(self, *args, **kwargs):
        
        self.attr1 = kwargs.get('arg1')
        self.attr2 = kwargs.get('arg2')

    def attribute_addition(self):
        """
        This is the docstring: it contains the description of the method
        It could also contain a doctest

        doctest:
        >>> my_class_instance = MyClass(arg1=1,arg2=2)
        >>> my_class_instance.attribute_addition()
        3
        """

        return self.attr1 + self.attr2

    def __repr__(self):
        """
        This is a method that returns the instance information
        It's called when my_class_instance is called
        E.g.: print(my_class_instance)
        
        """
        return (f"1st. attrubute is {self.attr1} "
               +f"2nd. attrubute is {self.attr2}")

if __name__ == "__main__":
    c1 = MyClass(arg1=1,arg2=2,arg3=3)
    print("C1: ", c1)
    c2 = MyClass(arg2="4")
    print("C2: ", c2)
    