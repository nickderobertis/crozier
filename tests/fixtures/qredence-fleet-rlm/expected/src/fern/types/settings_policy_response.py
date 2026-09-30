

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .settings_scope_response import SettingsScopeResponse


class SettingsPolicyResponse(UniversalBaseModel):
    revision: str
    active_profile: typing.Optional[str] = None
    default_profile: typing.Optional[str] = None
    available_profiles: typing.Optional[typing.List[str]] = None
    restart_required: typing.Optional[bool] = None
    scopes: typing.List[SettingsScopeResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
