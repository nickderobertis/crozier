

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .instant import Instant
from .severity import Severity


class AlertEventResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    rule_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ruleId"), pydantic.Field(alias="ruleId")
    ] = None
    rule_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ruleName"), pydantic.Field(alias="ruleName")
    ] = None
    pipeline_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pipelineId"), pydantic.Field(alias="pipelineId")
    ] = None
    pipeline_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pipelineName"), pydantic.Field(alias="pipelineName")
    ] = None
    status: typing.Optional[str] = None
    value: typing.Optional[float] = None
    threshold: typing.Optional[float] = None
    severity: typing.Optional[Severity] = None
    message: typing.Optional[str] = None
    fired_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="firedAt"), pydantic.Field(alias="firedAt")
    ] = None
    resolved_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="resolvedAt"), pydantic.Field(alias="resolvedAt")
    ] = None
    duration_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="durationSeconds"), pydantic.Field(alias="durationSeconds")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
