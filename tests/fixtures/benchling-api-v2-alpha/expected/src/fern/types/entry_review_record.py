

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_review_process import EntryReviewProcess
from .entry_review_record_status import EntryReviewRecordStatus
from .review_change import ReviewChange


class EntryReviewRecord(UniversalBaseModel):
    """
    Review record if set
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reviewer's Comments
    """

    review_changes: typing_extensions.Annotated[
        typing.Optional[typing.List[ReviewChange]],
        FieldMetadata(alias="reviewChanges"),
        pydantic.Field(
            alias="reviewChanges", description="A list of the Review Changes that have been made to this entry"
        ),
    ] = None
    """
    A list of the Review Changes that have been made to this entry
    """

    review_processes: typing_extensions.Annotated[
        typing.Optional[typing.List[EntryReviewProcess]],
        FieldMetadata(alias="reviewProcesses"),
        pydantic.Field(alias="reviewProcesses", description="Review Processes associated with the Entry"),
    ] = None
    """
    Review Processes associated with the Entry
    """

    status: typing.Optional[EntryReviewRecordStatus] = pydantic.Field(default=None)
    """
    Review Status of the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
