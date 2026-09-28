

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_llm_response_chaos_truncate_mode import HttpLlmResponseChaosTruncateMode


class HttpLlmResponseChaos(UniversalBaseModel):
    error_status: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="errorStatus"), pydantic.Field(alias="errorStatus")
    ] = None
    retry_after: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="retryAfter"), pydantic.Field(alias="retryAfter")
    ] = None
    error_probability: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="errorProbability"), pydantic.Field(alias="errorProbability")
    ] = None
    truncate_mode: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponseChaosTruncateMode],
        FieldMetadata(alias="truncateMode"),
        pydantic.Field(alias="truncateMode"),
    ] = None
    truncate_at_fraction: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="truncateAtFraction"), pydantic.Field(alias="truncateAtFraction")
    ] = None
    malformed_sse: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="malformedSse"), pydantic.Field(alias="malformedSse")
    ] = None
    seed: typing.Optional[int] = None
    quota_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="quotaName"), pydantic.Field(alias="quotaName")
    ] = None
    quota_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="quotaLimit"), pydantic.Field(alias="quotaLimit")
    ] = None
    quota_window_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="quotaWindowMillis"), pydantic.Field(alias="quotaWindowMillis")
    ] = None
    quota_error_status: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="quotaErrorStatus"), pydantic.Field(alias="quotaErrorStatus")
    ] = None
    token_quota_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tokenQuotaLimit"), pydantic.Field(alias="tokenQuotaLimit")
    ] = None
    token_quota_window_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="tokenQuotaWindowMillis"),
        pydantic.Field(alias="tokenQuotaWindowMillis"),
    ] = None
    content_filter_block_probability: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="contentFilterBlockProbability"),
        pydantic.Field(alias="contentFilterBlockProbability"),
    ] = None
    error_kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorKind"), pydantic.Field(alias="errorKind")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
