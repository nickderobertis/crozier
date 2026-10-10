

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Weave_Joined(UniversalBaseModel):
    kind: typing.Literal["joined"] = "joined"
    threads: typing.Optional["Thread"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Weave_Loose(UniversalBaseModel):
    kind: typing.Literal["loose"] = "loose"
    length: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Weave = typing_extensions.Annotated[typing.Union[Weave_Joined, Weave_Loose], pydantic.Field(discriminator="kind")]
from .thread import Thread
from .thread_woven import ThreadWoven

update_forward_refs(Weave_Joined, Thread=Thread, ThreadWoven=ThreadWoven, Weave=Weave)
