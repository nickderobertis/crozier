

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OpenIdConnectSecurityScheme(UniversalBaseModel):
    """
    Defines a security scheme using OpenID Connect.
    """

    description: typing.Optional[str] = None
    open_id_connect_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="openIdConnectUrl"), pydantic.Field(alias="openIdConnectUrl")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
