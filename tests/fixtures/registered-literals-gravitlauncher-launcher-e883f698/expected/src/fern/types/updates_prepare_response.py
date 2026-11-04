

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdatesPrepareResponse(UniversalBaseModel):
    """
    Contains an opaque data blob to be signed by the build private key, plus a JWT token that must be echoed back in /updates/check.
    """

    data: str = pydantic.Field()
    """
    Base64-encoded bytes to sign with the ECDSA build private key.
    """

    jwt_token: typing_extensions.Annotated[str, FieldMetadata(alias="jwtToken"), pydantic.Field(alias="jwtToken")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
