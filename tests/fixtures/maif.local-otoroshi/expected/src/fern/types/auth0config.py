

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Auth0Config(UniversalBaseModel):
    """
    Configuration for Auth0 domain
    """

    callback_url: typing_extensions.Annotated[str, FieldMetadata(alias="callbackUrl")] = pydantic.Field()
    """
    Auth0 callback URL
    """

    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId")] = pydantic.Field()
    """
    Auth0 client id
    """

    client_secret: typing_extensions.Annotated[str, FieldMetadata(alias="clientSecret")] = pydantic.Field()
    """
    Auth0 client secret
    """

    domain: str = pydantic.Field()
    """
    Auth0 domain
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
