

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AttachmentUrl(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file type of attachment.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL where the attachment can be downloaded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
