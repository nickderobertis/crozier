

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_review_process_completion_status import EntryReviewProcessCompletionStatus
from .entry_review_process_stages_item import EntryReviewProcessStagesItem
from .entry_review_process_type import EntryReviewProcessType


class EntryReviewProcess(UniversalBaseModel):
    completion_status: typing_extensions.Annotated[
        typing.Optional[EntryReviewProcessCompletionStatus],
        FieldMetadata(alias="completionStatus"),
        pydantic.Field(alias="completionStatus", description="State of the Entry at the end of the Review Process"),
    ] = None
    """
    State of the Entry at the end of the Review Process
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the Review Process
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Review Process
    """

    stages: typing.Optional[typing.List[EntryReviewProcessStagesItem]] = pydantic.Field(default=None)
    """
    Array of Stages for the Review Process
    """

    type: typing.Optional[EntryReviewProcessType] = pydantic.Field(default=None)
    """
    Type of the Review Process
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
