

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_summary import ChannelSummary
from .duration import Duration
from .instant import Instant
from .operator import Operator
from .reduce_function import ReduceFunction
from .severity import Severity


class AlertRuleResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    panel_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="panelId"), pydantic.Field(alias="panelId")
    ] = None
    panel_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="panelTitle"), pydantic.Field(alias="panelTitle")
    ] = None
    operator: typing.Optional[Operator] = None
    threshold: typing.Optional[float] = None
    for_duration: typing_extensions.Annotated[
        typing.Optional[Duration],
        FieldMetadata(alias="forDuration"),
        pydantic.Field(
            alias="forDuration", description="ISO-8601 duration for how long the condition must hold before firing"
        ),
    ] = None
    """
    ISO-8601 duration for how long the condition must hold before firing
    """

    reduce_function: typing_extensions.Annotated[
        typing.Optional[ReduceFunction], FieldMetadata(alias="reduceFunction"), pydantic.Field(alias="reduceFunction")
    ] = None
    evaluation_window: typing_extensions.Annotated[
        typing.Optional[Duration],
        FieldMetadata(alias="evaluationWindow"),
        pydantic.Field(alias="evaluationWindow", description="ISO-8601 duration for the evaluation window"),
    ] = None
    """
    ISO-8601 duration for the evaluation window
    """

    severity: typing.Optional[Severity] = None
    enabled: typing.Optional[bool] = None
    channels: typing.Optional[typing.List[ChannelSummary]] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
