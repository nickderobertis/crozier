

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .composite_signature_binding import CompositeSignatureBinding
from .composite_signature_classical import CompositeSignatureClassical
from .composite_signature_pq import CompositeSignaturePq


class CompositeSignature(UniversalBaseModel):
    classical: typing.Optional[CompositeSignatureClassical] = None
    pq: typing.Optional[CompositeSignaturePq] = None
    binding: typing.Optional[CompositeSignatureBinding] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
