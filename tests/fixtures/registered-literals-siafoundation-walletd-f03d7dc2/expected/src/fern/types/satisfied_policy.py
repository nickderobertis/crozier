

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signature import Signature
from .spend_policy import SpendPolicy


class SatisfiedPolicy(UniversalBaseModel):
    policy: SpendPolicy
    signatures: typing.Optional[typing.List[Signature]] = None
    preimages: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
