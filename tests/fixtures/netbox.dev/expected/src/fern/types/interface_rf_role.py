

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_rf_role_label import InterfaceRfRoleLabel
from .interface_rf_role_value import InterfaceRfRoleValue


class InterfaceRfRole(UniversalBaseModel):
    label: InterfaceRfRoleLabel
    value: InterfaceRfRoleValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
