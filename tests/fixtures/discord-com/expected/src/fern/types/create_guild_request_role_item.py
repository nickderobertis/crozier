

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateGuildRequestRoleItem(UniversalBaseModel):
    id: int
    name: typing.Optional[str] = None
    permissions: typing.Optional[int] = None
    color: typing.Optional[int] = None
    hoist: typing.Optional[bool] = None
    mentionable: typing.Optional[bool] = None
    unicode_emoji: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
