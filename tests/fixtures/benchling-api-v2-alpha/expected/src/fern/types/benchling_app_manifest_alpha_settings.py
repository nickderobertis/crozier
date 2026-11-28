

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .benchling_app_manifest_alpha_settings_lifecycle_management import (
    BenchlingAppManifestAlphaSettingsLifecycleManagement,
)


class BenchlingAppManifestAlphaSettings(UniversalBaseModel):
    canvas_webhook_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="canvasWebhookUrl"),
        pydantic.Field(
            alias="canvasWebhookUrl",
            description="URL that Benchling sends app canvas payloads to. It will override the default webhookUrl This destination should be backed by an endpoint owned by your application.",
        ),
    ] = None
    """
    URL that Benchling sends app canvas payloads to. It will override the default webhookUrl This destination should be backed by an endpoint owned by your application.
    """

    lifecycle_management: typing_extensions.Annotated[
        typing.Optional[BenchlingAppManifestAlphaSettingsLifecycleManagement],
        FieldMetadata(alias="lifecycleManagement"),
        pydantic.Field(
            alias="lifecycleManagement",
            description="Specify whether app will be activated automatically or manually. If automatic is specified, a webhook url is required.",
        ),
    ] = None
    """
    Specify whether app will be activated automatically or manually. If automatic is specified, a webhook url is required.
    """

    lifecycle_webhook_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lifecycleWebhookUrl"),
        pydantic.Field(
            alias="lifecycleWebhookUrl",
            description="URL that Benchling sends app lifecycle payloads to. It will override the default webhookUrl This destination should be backed by an endpoint owned by your application.",
        ),
    ] = None
    """
    URL that Benchling sends app lifecycle payloads to. It will override the default webhookUrl This destination should be backed by an endpoint owned by your application.
    """

    webhook_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookUrl"),
        pydantic.Field(
            alias="webhookUrl",
            description="URL that Benchling sends app interaction payloads to. This is the default URL if no other webhook URLs are specified in the app's manifest. This destination should be backed by an endpoint owned by your application.",
        ),
    ] = None
    """
    URL that Benchling sends app interaction payloads to. This is the default URL if no other webhook URLs are specified in the app's manifest. This destination should be backed by an endpoint owned by your application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
