class StructureB(object):
    """
    Base structure class for basketball classes.
      Structure{B}, B stands for basketball.
    Checks whether the inherited <_fields> correspond to the declared type
    and stores them in relevant attributes.
    """

    _fields = []

    def _init_arg(self, expected_type, value):
        if isinstance(value, expected_type) or value is None: # IMPORTANT we also accept None values
            return value
        else:
            return expected_type(**value)

    def __init__(self, **kwargs):
        field_names, field_types = zip(*self._fields)
        assert([isinstance(name, str) for name in field_names])
        assert([isinstance(type_, type) for type_ in field_types])

        for name, field_type in self._fields:
            setattr(self, name, self._init_arg(field_type, kwargs.pop(name)))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Class init error: Invalid argument(s): {}'.format(','.join(kwargs)))
