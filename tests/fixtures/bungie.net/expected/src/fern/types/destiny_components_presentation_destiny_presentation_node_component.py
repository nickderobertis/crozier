

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyComponentsPresentationDestinyPresentationNodeComponent(UniversalBaseModel):
    completion_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="completionValue"),
        pydantic.Field(
            alias="completionValue",
            description="The value at which the presentation node is considered to be completed.",
        ),
    ] = None
    """
    The value at which the presentation node is considered to be completed.
    """

    objective: typing.Optional[DestinyQuestsDestinyObjectiveProgress] = pydantic.Field(default=None)
    """
    An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes.
    """

    progress_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressValue"),
        pydantic.Field(
            alias="progressValue",
            description="How much of the presentation node is considered to be completed so far by the given character/profile.",
        ),
    ] = None
    """
    How much of the presentation node is considered to be completed so far by the given character/profile.
    """

    record_category_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="recordCategoryScore"),
        pydantic.Field(
            alias="recordCategoryScore",
            description="If available, this is the current score for the record category that this node represents.",
        ),
    ] = None
    """
    If available, this is the current score for the record category that this node represents.
    """

    state: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
