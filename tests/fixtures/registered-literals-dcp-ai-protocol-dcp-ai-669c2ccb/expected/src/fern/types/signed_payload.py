

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .composite_signature import CompositeSignature


class SignedPayload(UniversalBaseModel):
    payload: typing.Dict[str, typing.Any]
    payload_hash: typing.Optional[str] = None
    composite_sig: CompositeSignature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
