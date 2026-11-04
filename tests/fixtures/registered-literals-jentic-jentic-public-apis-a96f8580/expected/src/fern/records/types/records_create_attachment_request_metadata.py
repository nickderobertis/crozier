

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RecordsCreateAttachmentRequestMetadata(UniversalBaseModel):
    """
    The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the file. Must have a supported file extension (.adoc, .asice, .bdoc, .csv, .ddoc, .doc, .docx, .edoc, .eml, .gif, .htm, .jpeg, .jpg, .msg, .pdf, .png, .ppt, .pptx, .rtf,.tif, .txt, .xls, .xlsx, .xml).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
