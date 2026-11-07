

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .siafund_output import SiafundOutput
from .siafund_output_id import SiafundOutputId


class SiafundOutputWithId(SiafundOutput):
    id: SiafundOutputId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
