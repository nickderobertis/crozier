

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NoteAttachmentRequestResponse(UniversalBaseModel):
    attachment_id: int = pydantic.Field()
    """
    The reference to the uploaded file to attach to this note.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the attachment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
