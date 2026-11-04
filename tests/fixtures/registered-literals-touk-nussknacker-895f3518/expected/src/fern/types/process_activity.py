

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment1 import Attachment1
from .comment import Comment


class ProcessActivity(UniversalBaseModel):
    comments: typing.Optional[typing.List[Comment]] = None
    attachments: typing.Optional[typing.List[Attachment1]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
