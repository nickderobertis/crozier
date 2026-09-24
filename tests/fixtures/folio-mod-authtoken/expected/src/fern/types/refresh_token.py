

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RefreshToken(UniversalBaseModel):
    """
    The refresh token being presented to get a new refresh token and access token
    """

    refresh_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="refreshToken"),
        pydantic.Field(alias="refreshToken", description="The JWE refresh token"),
    ]
    """
    The JWE refresh token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
