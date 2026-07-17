

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSource(enum.StrEnum):
    RESOURCE_REFERENCE = "ResourceReference"
    PARAMETER_REFERENCE = "ParameterReference"
    RESOURCE_ATTRIBUTE = "ResourceAttribute"
    DIRECT_MODIFICATION = "DirectModification"
    AUTOMATIC = "Automatic"

    def visit(
        self,
        resource_reference: typing.Callable[[], T_Result],
        parameter_reference: typing.Callable[[], T_Result],
        resource_attribute: typing.Callable[[], T_Result],
        direct_modification: typing.Callable[[], T_Result],
        automatic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSource.RESOURCE_REFERENCE:
            return resource_reference()
        if self is ChangeSource.PARAMETER_REFERENCE:
            return parameter_reference()
        if self is ChangeSource.RESOURCE_ATTRIBUTE:
            return resource_attribute()
        if self is ChangeSource.DIRECT_MODIFICATION:
            return direct_modification()
        if self is ChangeSource.AUTOMATIC:
            return automatic()
