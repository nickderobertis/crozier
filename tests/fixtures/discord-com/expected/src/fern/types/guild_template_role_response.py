

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GuildTemplateRoleResponse(UniversalBaseModel):
    id: int
    name: str
    permissions: str
    color: int
    hoist: bool
    mentionable: bool
    icon: typing.Optional[str] = None
    unicode_emoji: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
