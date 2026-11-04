

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebAuthnAssertionResponse(UniversalBaseModel):
    client_data_json: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientDataJSON"), pydantic.Field(alias="clientDataJSON", description="base64url")
    ]
    """
    base64url
    """

    authenticator_data: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authenticatorData"),
        pydantic.Field(alias="authenticatorData", description="base64url"),
    ]
    """
    base64url
    """

    signature: str = pydantic.Field()
    """
    base64url
    """

    user_handle: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userHandle"),
        pydantic.Field(alias="userHandle", description="base64url"),
    ] = None
    """
    base64url
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
