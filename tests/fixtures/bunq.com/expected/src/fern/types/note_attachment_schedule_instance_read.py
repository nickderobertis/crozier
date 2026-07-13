

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from .label_user import LabelUser


class NoteAttachmentScheduleInstanceRead(UniversalBaseModel):
    attachment: typing.Optional[typing.List[AttachmentMonetaryAccountPayment]] = pydantic.Field(default=None)
    """
    The attachment attached to the note.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the note's creation.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the attachment.
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
