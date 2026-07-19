

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DsseSchemaSignaturesItem(UniversalBaseModel):
    """
    a signature of the envelope's payload along with the verification material for the signature
    """

    signature: str = pydantic.Field()
    """
    base64 encoded signature of the payload
    """

    verifier: str = pydantic.Field()
    """
    verification material that was used to verify the corresponding signature, specified as a base64 encoded string
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
