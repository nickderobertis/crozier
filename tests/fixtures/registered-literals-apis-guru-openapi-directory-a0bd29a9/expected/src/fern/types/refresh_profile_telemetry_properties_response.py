

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profile_specifier import ProfileSpecifier


class RefreshProfileTelemetryPropertiesResponse(UniversalBaseModel):
    failed: typing.Optional[typing.List[ProfileSpecifier]] = None
    succeeded: typing.Optional[typing.List[ProfileSpecifier]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
