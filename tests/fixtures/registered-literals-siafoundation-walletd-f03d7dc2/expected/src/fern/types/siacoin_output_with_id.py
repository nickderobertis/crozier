

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .siacoin_output import SiacoinOutput
from .siacoin_output_id import SiacoinOutputId


class SiacoinOutputWithId(SiacoinOutput):
    id: SiacoinOutputId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
