

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LoadScenarioReportCounts(UniversalBaseModel):
    requests_sent: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="requestsSent"), pydantic.Field(alias="requestsSent")
    ] = None
    succeeded: typing.Optional[int] = None
    failed: typing.Optional[int] = None
    dropped_iterations: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="droppedIterations"), pydantic.Field(alias="droppedIterations")
    ] = None
    error_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="errorRate"),
        pydantic.Field(alias="errorRate", description="failed / max(1, requestsSent)"),
    ] = None
    """
    failed / max(1, requestsSent)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
