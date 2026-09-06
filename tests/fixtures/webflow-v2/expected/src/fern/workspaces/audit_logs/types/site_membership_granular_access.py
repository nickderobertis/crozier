

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .site_membership_granular_access_type import SiteMembershipGranularAccessType


class SiteMembershipGranularAccess(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    type: typing.Optional[SiteMembershipGranularAccessType] = None
    restricted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
