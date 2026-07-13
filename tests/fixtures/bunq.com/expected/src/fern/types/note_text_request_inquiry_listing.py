

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class NoteTextRequestInquiryListing(UniversalBaseModel):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the note.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the note's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the note.
    """

    label_user_creator: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user who created this note.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the note's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
