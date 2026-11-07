

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .global_config_response_ai import GlobalConfigResponseAi
from .global_config_response_observability import GlobalConfigResponseObservability


class GlobalConfigResponse(UniversalBaseModel):
    allow_register: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowRegister"), pydantic.Field(alias="allowRegister")
    ]
    website_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteId"), pydantic.Field(alias="websiteId")
    ] = None
    amap_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="amapToken"), pydantic.Field(alias="amapToken")
    ] = None
    mapbox_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mapboxToken"), pydantic.Field(alias="mapboxToken")
    ] = None
    alpha_mode: typing_extensions.Annotated[bool, FieldMetadata(alias="alphaMode"), pydantic.Field(alias="alphaMode")]
    disable_anonymous_telemetry: typing_extensions.Annotated[
        bool, FieldMetadata(alias="disableAnonymousTelemetry"), pydantic.Field(alias="disableAnonymousTelemetry")
    ]
    custom_tracker_script_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customTrackerScriptName"),
        pydantic.Field(alias="customTrackerScriptName"),
    ] = None
    server_timezone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="serverTimezone"), pydantic.Field(alias="serverTimezone")
    ] = None
    auth_provider: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="authProvider"), pydantic.Field(alias="authProvider")
    ]
    custom_auth_provider_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customAuthProviderIcon"),
        pydantic.Field(alias="customAuthProviderIcon"),
    ] = None
    smtp_available: typing_extensions.Annotated[
        bool, FieldMetadata(alias="smtpAvailable"), pydantic.Field(alias="smtpAvailable")
    ]
    enable_billing: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableBilling"), pydantic.Field(alias="enableBilling")
    ]
    ai: GlobalConfigResponseAi
    enable_function_worker: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableFunctionWorker"), pydantic.Field(alias="enableFunctionWorker")
    ]
    observability: GlobalConfigResponseObservability

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
