

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventActionEmailConfig(UniversalBaseModel):
    recipients: typing.Optional[typing.List[str]] = None
    bcc: typing.Optional[typing.List[str]] = None
    subject: typing.Optional[str] = None
    body: typing.Optional[str] = None
    content_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Content type:
      * `0` text/plain
      * `1` text/html
    """

    attachments: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of file paths to attach. The total size is limited to 10 MB
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
