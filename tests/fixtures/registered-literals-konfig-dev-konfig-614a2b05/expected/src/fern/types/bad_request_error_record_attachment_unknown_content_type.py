

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorRecordAttachmentUnknownContentType(UniversalBaseModel):
    """
    Bad request error. Unknown content type.
    """

    code: typing.Optional[str] = None
    message: typing.Optional[str] = None
    param: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
