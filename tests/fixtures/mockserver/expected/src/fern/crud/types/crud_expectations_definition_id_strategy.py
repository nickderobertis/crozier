

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CrudExpectationsDefinitionIdStrategy(enum.StrEnum):
    """
    strategy used to generate identifiers for newly created resources
    """

    AUTO_INCREMENT = "AUTO_INCREMENT"
    UUID = "UUID"

    def visit(self, auto_increment: typing.Callable[[], T_Result], uuid_: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrudExpectationsDefinitionIdStrategy.AUTO_INCREMENT:
            return auto_increment()
        if self is CrudExpectationsDefinitionIdStrategy.UUID:
            return uuid_()
