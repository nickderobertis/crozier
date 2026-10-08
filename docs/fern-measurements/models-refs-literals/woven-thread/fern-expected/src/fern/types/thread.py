

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Thread_Woven(UniversalBaseModel):
    kind: typing.Literal["woven"] = "woven"
    weave: typing.Optional["Weave"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Thread_Plain(UniversalBaseModel):
    kind: typing.Literal["plain"] = "plain"
    color: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Thread = typing_extensions.Annotated[typing.Union[Thread_Woven, Thread_Plain], pydantic.Field(discriminator="kind")]
from .weave import Weave
from .weave_joined import WeaveJoined

update_forward_refs(Thread_Woven, Thread=Thread, Weave=Weave, WeaveJoined=WeaveJoined)
