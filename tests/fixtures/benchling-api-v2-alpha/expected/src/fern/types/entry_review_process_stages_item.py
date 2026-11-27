

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_review_process_stages_item_action_label import EntryReviewProcessStagesItemActionLabel
from .entry_review_process_stages_item_reviewers_item import EntryReviewProcessStagesItemReviewersItem


class EntryReviewProcessStagesItem(UniversalBaseModel):
    action_label: typing_extensions.Annotated[
        typing.Optional[EntryReviewProcessStagesItemActionLabel],
        FieldMetadata(alias="actionLabel"),
        pydantic.Field(alias="actionLabel", description="Action reviewer is doing during the review"),
    ] = None
    """
    Action reviewer is doing during the review
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the Review Stage
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Review Stage
    """

    reviewers: typing.Optional[typing.List[EntryReviewProcessStagesItemReviewersItem]] = pydantic.Field(default=None)
    """
    Reviewers for the Review Stage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
