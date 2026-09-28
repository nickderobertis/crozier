

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_webhook_type import OtoroshiModelsWebhookType


class OtoroshiModelsWebhook(UniversalBaseModel):
    """
    Settings for webhook call
    """

    type: typing.Optional[OtoroshiModelsWebhookType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL where events are posted
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Headers to authorize the call or whatever
    """

    mtls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="mtlsConfig"), pydantic.Field(alias="mtlsConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
