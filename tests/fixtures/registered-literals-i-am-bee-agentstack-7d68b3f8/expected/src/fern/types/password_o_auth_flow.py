

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PasswordOAuthFlow(UniversalBaseModel):
    """
    Defines configuration details for the OAuth 2.0 Resource Owner Password flow.
    """

    refresh_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="refreshUrl"), pydantic.Field(alias="refreshUrl")
    ] = None
    scopes: typing.Dict[str, str]
    token_url: typing_extensions.Annotated[str, FieldMetadata(alias="tokenUrl"), pydantic.Field(alias="tokenUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
