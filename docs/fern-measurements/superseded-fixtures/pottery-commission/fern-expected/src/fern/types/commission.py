

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .ticketed import Ticketed


class Commission(Ticketed):
    glaze: str
    kiln_notes: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
