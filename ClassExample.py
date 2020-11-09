class Person(object):
    """A simple class."""
    species = "Homo Sapiens"
                                # docstring
                                #  class attribute
    def __init__(self, name):
        """This is the initializer. It's a special method (see below)."""
        self.name = name        # special method
        
    def __str__(self):
        """This method is run when Python tries to cast the object to a string. Return this string when using print(), etc. """
        return self.name        # special method
                                # instance attribute
    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))


        
staff = Person("Iam Vinu")
print(staff)
staff.rename("Raja")
print(staff)