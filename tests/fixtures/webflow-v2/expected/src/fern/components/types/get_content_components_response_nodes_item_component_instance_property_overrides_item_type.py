

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType(enum.StrEnum):
    """
    The type of the property.
    """

    PLAIN_TEXT = "Plain Text"
    RICH_TEXT = "Rich Text"
    ALT_TEXT = "Alt Text"

    def visit(
        self,
        plain_text: typing.Callable[[], T_Result],
        rich_text: typing.Callable[[], T_Result],
        alt_text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType.PLAIN_TEXT:
            return plain_text()
        if self is GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType.RICH_TEXT:
            return rich_text()
        if self is GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItemType.ALT_TEXT:
            return alt_text()
