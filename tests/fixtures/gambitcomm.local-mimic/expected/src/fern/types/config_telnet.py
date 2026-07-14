

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigTelnet(UniversalBaseModel):
    keymap: typing.Optional[str] = None
    paging_prompt: typing.Optional[str] = None
    port: typing.Optional[int] = None
    prompt: typing.Optional[str] = None
    rule: typing.Optional[str] = None
    userdb: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
