

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DsseSchemaProposedContent(UniversalBaseModel):
    envelope: str = pydantic.Field()
    """
    DSSE envelope specified as a stringified JSON object
    """

    verifiers: typing.List[str] = pydantic.Field()
    """
    collection of all verification material (e.g. public keys or certificates) used to verify signatures over envelope's payload, specified as base64-encoded strings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
