

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flavours_quota import FlavoursQuota


class ProjectFlavoursQuota(UniversalBaseModel):
    name: str
    proj_key: str
    quotas: typing.List[FlavoursQuota]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
