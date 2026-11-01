

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .username import Username


class UserState_Unintroduced(UniversalBaseModel):
    status: typing.Literal["unintroduced"] = "unintroduced"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UserState_Introduced(UniversalBaseModel):
    status: typing.Literal["introduced"] = "introduced"
    username: Username

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UserState = typing_extensions.Annotated[
    typing.Union[UserState_Unintroduced, UserState_Introduced], pydantic.Field(discriminator="status")
]
