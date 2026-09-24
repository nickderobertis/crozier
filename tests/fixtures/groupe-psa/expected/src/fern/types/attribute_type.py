

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AttributeType(enum.StrEnum):
    """
    3 attributes type:

    |Attribute-type|Role|
    |----------|-------------|
    |Header|-Will be add as http header extension "x-######:"|
    |Body|-Will be simply add to event body map attribute (see monitor event definition in template document)|
    |Query|-Will set as http query parameter when invoking the Webhook|
    """

    HEADER = "Header"
    BODY = "Body"
    QUERY = "Query"

    def visit(
        self,
        header: typing.Callable[[], T_Result],
        body: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AttributeType.HEADER:
            return header()
        if self is AttributeType.BODY:
            return body()
        if self is AttributeType.QUERY:
            return query()
