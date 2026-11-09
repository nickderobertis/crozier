

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccessTokenResponse(UniversalBaseModel):
    access_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accessToken"),
        pydantic.Field(alias="accessToken", description="Access token for API."),
    ]
    """
    Access token for API.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    token_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tokenId"),
        pydantic.Field(alias="tokenId", description="Unique Id for the access token."),
    ]
    """
    Unique Id for the access token.
    """

    token_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="tokenType"), pydantic.Field(alias="tokenType", description="Token type.")
    ]
    """
    Token type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
