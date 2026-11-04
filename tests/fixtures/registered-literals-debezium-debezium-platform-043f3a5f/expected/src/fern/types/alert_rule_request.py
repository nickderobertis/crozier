

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .duration import Duration
from .operator import Operator
from .reduce_function import ReduceFunction
from .severity import Severity


class AlertRuleRequest(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    panel_id: typing_extensions.Annotated[str, FieldMetadata(alias="panelId"), pydantic.Field(alias="panelId")]
    operator: Operator
    threshold: float
    for_duration: typing_extensions.Annotated[
        typing.Optional[Duration],
        FieldMetadata(alias="forDuration"),
        pydantic.Field(
            alias="forDuration",
            description="ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H",
        ),
    ] = None
    """
    ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H
    """

    reduce_function: typing_extensions.Annotated[
        typing.Optional[ReduceFunction], FieldMetadata(alias="reduceFunction"), pydantic.Field(alias="reduceFunction")
    ] = None
    evaluation_window: typing_extensions.Annotated[
        typing.Optional[Duration],
        FieldMetadata(alias="evaluationWindow"),
        pydantic.Field(
            alias="evaluationWindow",
            description="ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H",
        ),
    ] = None
    """
    ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H
    """

    severity: typing.Optional[Severity] = None
    enabled: typing.Optional[bool] = None
    channel_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="channelIds"), pydantic.Field(alias="channelIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
