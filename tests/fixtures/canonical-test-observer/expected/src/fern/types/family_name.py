

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FamilyName(enum.StrEnum):
    SNAP = "snap"
    DEB = "deb"
    CHARM = "charm"
    IMAGE = "image"
    SOLUTION = "solution"

    def visit(
        self,
        snap: typing.Callable[[], T_Result],
        deb: typing.Callable[[], T_Result],
        charm: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        solution: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FamilyName.SNAP:
            return snap()
        if self is FamilyName.DEB:
            return deb()
        if self is FamilyName.CHARM:
            return charm()
        if self is FamilyName.IMAGE:
            return image()
        if self is FamilyName.SOLUTION:
            return solution()
