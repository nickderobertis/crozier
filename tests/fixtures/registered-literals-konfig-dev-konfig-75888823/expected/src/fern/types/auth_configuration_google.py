

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthConfigurationGoogle(UniversalBaseModel):
    """
    Enable google auth for your application.
    """

    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId",
            description="A Google generated token representing the developer's credentials for [Google's API Console](https://console.cloud.google.com/apis/dashboard?pli=1&project=discourse-login-388921). Learn how to get a `clientId` [here](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid).",
        ),
    ]
    """
    A Google generated token representing the developer's credentials for [Google's API Console](https://console.cloud.google.com/apis/dashboard?pli=1&project=discourse-login-388921). Learn how to get a `clientId` [here](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
