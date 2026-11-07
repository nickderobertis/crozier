

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettingsInfo(UniversalBaseModel):
    ui_backend_api_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uiBackendApiPath"), pydantic.Field(alias="uiBackendApiPath")
    ] = None
    read_result_summary_polling_interval: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="readResultSummaryPollingInterval"),
        pydantic.Field(alias="readResultSummaryPollingInterval"),
    ] = None
    read_result_detailed_obfuscated_polling_interval: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="readResultDetailedObfuscatedPollingInterval"),
        pydantic.Field(alias="readResultDetailedObfuscatedPollingInterval"),
    ] = None
    read_result_detailed_obfuscated_amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="readResultDetailedObfuscatedAmount"),
        pydantic.Field(alias="readResultDetailedObfuscatedAmount"),
    ] = None
    read_result_detailed_obfuscated_interval: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="readResultDetailedObfuscatedInterval"),
        pydantic.Field(alias="readResultDetailedObfuscatedInterval"),
    ] = None
    passthrough_polling_time_ui: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="passthroughPollingTimeUi"),
        pydantic.Field(alias="passthroughPollingTimeUi"),
    ] = None
    passthrough_ccdl_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="passthroughCcdlVersion"),
        pydantic.Field(alias="passthroughCcdlVersion"),
    ] = None
    passthrough_portal_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="passthroughPortalLink"),
        pydantic.Field(alias="passthroughPortalLink"),
    ] = None
    passthrough_dse_patient_profile_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="passthroughDsePatientProfileUrl"),
        pydantic.Field(alias="passthroughDsePatientProfileUrl"),
    ] = None
    max_saved_queries_per_user: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxSavedQueriesPerUser"),
        pydantic.Field(alias="maxSavedQueriesPerUser"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
