

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_diff import FileDiff


class UserMessageSummary(UniversalBaseModel):
    title: typing.Optional[str] = None
    body: typing.Optional[str] = None
    diffs: typing.List[FileDiff]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
