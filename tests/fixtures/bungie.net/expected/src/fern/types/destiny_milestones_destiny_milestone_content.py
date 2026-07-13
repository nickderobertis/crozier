

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_milestone_content_item_category import (
    DestinyMilestonesDestinyMilestoneContentItemCategory,
)


class DestinyMilestonesDestinyMilestoneContent(UniversalBaseModel):
    """
    Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.
    """

    about: typing.Optional[str] = pydantic.Field(default=None)
    """
    The "About this Milestone" text from the Firehose.
    """

    item_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyMilestonesDestinyMilestoneContentItemCategory]],
        FieldMetadata(alias="itemCategories"),
    ] = pydantic.Field(default=None)
    """
    If DPS has defined items related to this Milestone, they can categorize those items in the Firehose. That data will then be returned as item categories here.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Current Status of the Milestone, as driven by the Firehose.
    """

    tips: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tips, provided by the Firehose.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
