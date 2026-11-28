

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntryAttachments(UniversalBaseModel):
    attachment_text: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="attachmentText"),
        pydantic.Field(
            alias="attachmentText",
            description='Text to include in the entry before the attachments. If not provided, the text will be "File attachments are listed below:"',
        ),
    ] = None
    """
    Text to include in the entry before the attachments. If not provided, the text will be "File attachments are listed below:"
    """

    attachments: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of IDs representing Blob objects in Benchling to be attached to the entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
