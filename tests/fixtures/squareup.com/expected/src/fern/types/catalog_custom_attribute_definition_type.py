

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CatalogCustomAttributeDefinitionType(str, enum.Enum):
    """
    Defines the possible types for a custom attribute.
    """

    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"
    SELECTION = "SELECTION"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        selection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogCustomAttributeDefinitionType.STRING:
            return string()
        if self is CatalogCustomAttributeDefinitionType.BOOLEAN:
            return boolean()
        if self is CatalogCustomAttributeDefinitionType.NUMBER:
            return number()
        if self is CatalogCustomAttributeDefinitionType.SELECTION:
            return selection()
