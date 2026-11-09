

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analysis import Analysis
from .license_decider import LicenseDecider
from .reuser import Reuser
from .scancode import Scancode


class ScanOptions(UniversalBaseModel):
    analysis: typing.Optional[Analysis] = None
    decider: typing.Optional[LicenseDecider] = None
    reuse: typing.Optional[Reuser] = None
    scancode: typing.Optional[Scancode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
