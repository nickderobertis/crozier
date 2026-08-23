

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .dpp_envelope import DppEnvelope


class DigitalProductPassportCompressed(DppEnvelope):
    """
    Compressed (operational) representation — EN 18223 clause 5.2. The envelope plus the product properties as key/value JSON, echoed as stored and carrying the operational `@context` that serves as the clause 5.2.2 data dictionary. Additional properties are the data elements keyed by name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
