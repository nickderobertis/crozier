

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role_select_default_value import RoleSelectDefaultValue


class RoleSelectComponentForMessageRequest(UniversalBaseModel):
    type: int
    custom_id: str
    placeholder: typing.Optional[str] = None
    min_values: typing.Optional[int] = None
    max_values: typing.Optional[int] = None
    disabled: typing.Optional[bool] = None
    default_values: typing.Optional[typing.List[RoleSelectDefaultValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
