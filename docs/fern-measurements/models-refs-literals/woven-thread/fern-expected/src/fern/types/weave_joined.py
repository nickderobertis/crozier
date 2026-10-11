

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class WeaveJoined(UniversalBaseModel):
    threads: typing.Optional["Thread"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thread import Thread
from .thread_woven import ThreadWoven
from .weave import Weave

update_forward_refs(WeaveJoined, Thread=Thread, ThreadWoven=ThreadWoven, Weave=Weave)
