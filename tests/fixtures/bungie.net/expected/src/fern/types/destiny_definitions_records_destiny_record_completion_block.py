

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsRecordsDestinyRecordCompletionBlock(UniversalBaseModel):
    score_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="ScoreValue")] = None
    partial_completion_objective_count_threshold: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="partialCompletionObjectiveCountThreshold")
    ] = pydantic.Field(default=None)
    """
    The number of objectives that must be completed before the objective is considered "complete"
    """

    should_fire_toast: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="shouldFireToast")] = None
    toast_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="toastStyle")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
