

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionConfigurationItemDefaultsItemTarget(enum.StrEnum):
    CUSTOM_FIELDS = "custom_fields"
    RESOURCE = "resource"

    def visit(self, custom_fields: typing.Callable[[], T_Result], resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionConfigurationItemDefaultsItemTarget.CUSTOM_FIELDS:
            return custom_fields()
        if self is ConnectionConfigurationItemDefaultsItemTarget.RESOURCE:
            return resource()
