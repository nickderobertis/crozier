

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .o_auth_flows import OAuthFlows


class OAuth2SecuritySchemeOutput(UniversalBaseModel):
    """
    Defines a security scheme using OAuth 2.0.
    """

    description: typing.Optional[str] = None
    flows: OAuthFlows
    oauth2metadata_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oauth2MetadataUrl"), pydantic.Field(alias="oauth2MetadataUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
