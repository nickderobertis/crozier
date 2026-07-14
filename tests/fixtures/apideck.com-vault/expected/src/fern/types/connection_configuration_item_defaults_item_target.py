

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionConfigurationItemDefaultsItemTarget(str, enum.Enum):
    CUSTOM_FIELDS = "custom_fields"
    RESOURCE = "resource"

    def visit(self, custom_fields: typing.Callable[[], T_Result], resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionConfigurationItemDefaultsItemTarget.CUSTOM_FIELDS:
            return custom_fields()
        if self is ConnectionConfigurationItemDefaultsItemTarget.RESOURCE:
            return resource()
