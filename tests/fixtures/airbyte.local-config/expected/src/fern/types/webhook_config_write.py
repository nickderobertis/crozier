

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebhookConfigWrite(UniversalBaseModel):
    auth_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="authToken")] = pydantic.Field(
        default=None
    )
    """
    an auth token, to be passed as the value for an HTTP Authorization header.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    human readable name for this webhook e.g. for UI display.
    """

    validation_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="validationUrl")] = (
        pydantic.Field(default=None)
    )
    """
    if supplied, the webhook config will be validated by checking that this URL returns a 2xx response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
