

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Attachment(UniversalBaseModel):
    base64: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, data must be encoded using base64. Otherwise, data will be interpreted as UTF-8
    """

    data: str = pydantic.Field()
    """
    Either plaintext or base64 encoded attachment data (depending on base64 field)
    """

    content_type: str = pydantic.Field()
    """
    The MIME type of the attachment
    """

    content_disposition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The disposition of the attachment
    """

    content_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content-ID that lets you reference this attachment as an inline image from your HTML.
    
    The value **must be wrapped in angle brackets**, matching the MIME `Content-ID` header format — for example `"<image1@example.com>"`. Reference it from `html_content` **without** the brackets, e.g. `<img src="cid:image1@example.com">`.
    
    If the angle brackets are omitted, the file is delivered as a regular (downloadable) attachment instead of rendering inline.
    """

    file_name: str = pydantic.Field()
    """
    The filename of the attachment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
