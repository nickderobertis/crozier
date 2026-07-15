

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NamespaceDefinitionType(str, enum.Enum):
    """
    Method used for computing final namespace in destination
    """

    SOURCE = "source"
    DESTINATION = "destination"
    CUSTOMFORMAT = "customformat"

    def visit(
        self,
        source: typing.Callable[[], T_Result],
        destination: typing.Callable[[], T_Result],
        customformat: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NamespaceDefinitionType.SOURCE:
            return source()
        if self is NamespaceDefinitionType.DESTINATION:
            return destination()
        if self is NamespaceDefinitionType.CUSTOMFORMAT:
            return customformat()
