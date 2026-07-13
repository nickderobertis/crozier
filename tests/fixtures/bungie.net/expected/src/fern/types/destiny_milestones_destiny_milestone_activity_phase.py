

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyMilestoneActivityPhase(UniversalBaseModel):
    """
    Represents whatever information we can return about an explicit phase in an activity. In the future, I hope we'll have more than just "guh, you done gone and did something," but for the forseeable future that's all we've got. I'm making it more than just a list of booleans out of that overly-optimistic hope.
    """

    complete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the phase has been completed.
    """

    phase_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="phaseHash")] = pydantic.Field(
        default=None
    )
    """
    In DestinyActivityDefinition, if the activity has phases, there will be a set of phases defined in the "insertionPoints" property. This is the hash that maps to that phase.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
