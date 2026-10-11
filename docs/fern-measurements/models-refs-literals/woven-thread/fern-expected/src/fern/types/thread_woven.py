

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ThreadWoven(UniversalBaseModel):
    weave: typing.Optional["Weave"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thread import Thread
from .weave import Weave
from .weave_joined import WeaveJoined

update_forward_refs(ThreadWoven, Thread=Thread, Weave=Weave, WeaveJoined=WeaveJoined)
