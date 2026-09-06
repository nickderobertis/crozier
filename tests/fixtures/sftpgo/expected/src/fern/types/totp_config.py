

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .totph_mac_algo import TotphMacAlgo


class TotpConfig(UniversalBaseModel):
    name: typing.Optional[str] = None
    issuer: typing.Optional[str] = None
    algo: typing.Optional[TotphMacAlgo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
