

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .obj2 import Obj2
from .obj3stuff import Obj3Stuff


class Obj3(Obj2):
    """
    some other stuff
    """

    height: typing.Optional[float] = None
    stuff: typing.Optional[Obj3Stuff] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Obj3)
