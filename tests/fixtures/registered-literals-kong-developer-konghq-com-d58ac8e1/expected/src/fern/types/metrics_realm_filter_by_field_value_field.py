

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsRealmFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    REALM = "realm"

    def visit(self, realm: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsRealmFilterByFieldValueField.REALM:
            return realm()
