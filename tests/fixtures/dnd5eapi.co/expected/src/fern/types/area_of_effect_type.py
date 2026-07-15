

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AreaOfEffectType(str, enum.Enum):
    SPHERE = "sphere"
    CONE = "cone"
    CYLINDER = "cylinder"
    LINE = "line"
    CUBE = "cube"

    def visit(
        self,
        sphere: typing.Callable[[], T_Result],
        cone: typing.Callable[[], T_Result],
        cylinder: typing.Callable[[], T_Result],
        line: typing.Callable[[], T_Result],
        cube: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AreaOfEffectType.SPHERE:
            return sphere()
        if self is AreaOfEffectType.CONE:
            return cone()
        if self is AreaOfEffectType.CYLINDER:
            return cylinder()
        if self is AreaOfEffectType.LINE:
            return line()
        if self is AreaOfEffectType.CUBE:
            return cube()
