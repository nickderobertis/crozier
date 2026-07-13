

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_milestone_content import DestinyMilestonesDestinyMilestoneContent
from .destiny_milestones_destiny_public_milestone import DestinyMilestonesDestinyPublicMilestone


class TrendingTrendingEntryDestinyRitual(UniversalBaseModel):
    date_end: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateEnd")] = None
    date_start: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateStart")] = None
    event_content: typing_extensions.Annotated[
        typing.Optional[DestinyMilestonesDestinyMilestoneContent], FieldMetadata(alias="eventContent")
    ] = pydantic.Field(default=None)
    """
    A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.
    """

    icon: typing.Optional[str] = None
    image: typing.Optional[str] = None
    milestone_details: typing_extensions.Annotated[
        typing.Optional[DestinyMilestonesDestinyPublicMilestone], FieldMetadata(alias="milestoneDetails")
    ] = pydantic.Field(default=None)
    """
    A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.
    """

    subtitle: typing.Optional[str] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
