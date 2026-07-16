

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Category(str, enum.Enum):
    REGISTERED = "REGISTERED"
    ACTIVATED = "ACTIVATED"
    THIRD_PARTY = "THIRD_PARTY"
    AWS_TYPES = "AWS_TYPES"

    def visit(
        self,
        registered: typing.Callable[[], T_Result],
        activated: typing.Callable[[], T_Result],
        third_party: typing.Callable[[], T_Result],
        aws_types: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Category.REGISTERED:
            return registered()
        if self is Category.ACTIVATED:
            return activated()
        if self is Category.THIRD_PARTY:
            return third_party()
        if self is Category.AWS_TYPES:
            return aws_types()
