

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostSetTypeConfigurationRequestAction(str, enum.Enum):
    SET_TYPE_CONFIGURATION = "SetTypeConfiguration"

    def visit(self, set_type_configuration: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSetTypeConfigurationRequestAction.SET_TYPE_CONFIGURATION:
            return set_type_configuration()
