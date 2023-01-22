class GlobalDefinableObject:
    """
    This class is used to define default values for the classes that inherit from it.
    Also, Users can pass their own priority values to the class via kwargs.
    """

    def __init__(self, **kwargs) -> None:
        for field in self.__class__.__dict__:
            if field.startswith("__"):
                continue

            if field in kwargs:
                continue

            setattr(self, field, getattr(self, field))

        for key, value in kwargs.items():
            setattr(self, key, value)
