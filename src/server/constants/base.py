class ConstantError(Exception):
    pass


class ConstantMeta(type):
    def __new__(meta_class, classname, bases, dict):
        sub_classes = [cls for cls in bases if isinstance(cls, ConstantMeta)]
        for sub_cls in sub_classes[1:]:
            if sub_classes[0] != sub_cls:
                raise ConstantError(
                    f"Can't inhelitance of [{sub_classes[0].__name__}] and [{sub_cls.__name__}] together"
                )

        super_constants = set()
        for base in bases:
            base_constants = ConstantMeta.__get_constant_attr(meta_class, base.__dict__)
            collisions = super_constants & base_constants
            if collisions:
                collisions_str = ", ".join(collisions)
                raise ConstantError(f"Collision the constant [{collisions_str}]")
            super_constants |= base_constants

        new_constants = ConstantMeta.__get_constant_attr(meta_class, dict)
        rebinds = super_constants & new_constants
        if rebinds:
            rebinds_str = ", ".join(rebinds)
            raise ConstantError(f"Can't rebind constant [{rebinds_str}]")

        def _meta__init__(self, *args, **kwargs):
            raise ConstantError("Can't make instance of Constant class")

        dict["__init__"] = _meta__init__

        return type.__new__(meta_class, classname, bases, dict)

    @staticmethod
    def __get_constant_attr(meta_class, dict):
        attrs = set(atr for atr in dict if not ConstantMeta.__is_special_func(atr))
        cnst_atr = set(atr for atr in attrs if meta_class.is_constant_attr(atr))
        var_atr = set(atr for atr in attrs if meta_class.is_settable_attr(atr))
        wrong_atr = attrs - (cnst_atr | var_atr)
        if wrong_atr:
            wrong_atr_str = ", ".join(wrong_atr)
            raise ConstantError(
                f"Attribute [{wrong_atr_str}] were not constant or not settable."
            )
        return cnst_atr

    @staticmethod
    def __is_special_func(name: str):
        return name.startswith("__") and name.endswith("__")

    @classmethod
    def is_constant_attr(meta_class, name: str):
        return not name.startswith("__")

    @classmethod
    def is_settable_attr(meta_class, name: str):
        return not meta_class.is_constant_attr(name)

    def __setattr__(cls, name, value):
        meta_class = type(cls)
        if meta_class.is_constant_attr(name) or (not meta_class.is_settable_attr(name)):
            raise ConstantError(f"Can't set attribute to Constant [{name}]")
        else:
            super().__setattr__(name, value)


class Constant(metaclass=ConstantMeta):
    pass
