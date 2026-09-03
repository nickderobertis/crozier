

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .process_status_status import ProcessStatusStatus


class ProcessStatus(UniversalBaseModel):
    process_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="processId"), pydantic.Field(alias="processId")
    ] = None
    current_step: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentStep"), pydantic.Field(alias="currentStep")
    ] = None
    completed_steps: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="completedSteps"), pydantic.Field(alias="completedSteps")
    ] = None
    overall_progress: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="overallProgress"),
        pydantic.Field(alias="overallProgress", description="Fortschritt in Prozent"),
    ] = None
    """
    Fortschritt in Prozent
    """

    status: typing.Optional[ProcessStatusStatus] = None
    estimated_completion: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="estimatedCompletion"),
        pydantic.Field(alias="estimatedCompletion"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
