

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FollowLevelsResponse_Flood(UniversalBaseModel):
    trend: typing.Literal["flood"] = "flood"
    height: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FollowLevelsResponse_Ebb(UniversalBaseModel):
    trend: typing.Literal["ebb"] = "ebb"
    height: typing.Optional[float] = None
    slack: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FollowLevelsResponse = typing_extensions.Annotated[
    typing.Union[FollowLevelsResponse_Flood, FollowLevelsResponse_Ebb], pydantic.Field(discriminator="trend")
]
