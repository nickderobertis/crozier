

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_create_attachments_review_record_status import EntryCreateAttachmentsReviewRecordStatus


class EntryCreateAttachmentsReviewRecord(UniversalBaseModel):
    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    User message to set on review
    """

    status: typing.Optional[EntryCreateAttachmentsReviewRecordStatus] = pydantic.Field(default=None)
    """
    Review Status for entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
