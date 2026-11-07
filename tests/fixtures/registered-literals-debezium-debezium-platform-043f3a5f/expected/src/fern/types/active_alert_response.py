

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_state_value import AlertStateValue
from .instant import Instant
from .severity import Severity


class ActiveAlertResponse(UniversalBaseModel):
    rule_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ruleId"), pydantic.Field(alias="ruleId")
    ] = None
    rule_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ruleName"), pydantic.Field(alias="ruleName")
    ] = None
    pipeline_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pipelineId"), pydantic.Field(alias="pipelineId")
    ] = None
    state: typing.Optional[AlertStateValue] = None
    severity: typing.Optional[Severity] = None
    value: typing.Optional[float] = None
    threshold: typing.Optional[float] = None
    since: typing.Optional[Instant] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
