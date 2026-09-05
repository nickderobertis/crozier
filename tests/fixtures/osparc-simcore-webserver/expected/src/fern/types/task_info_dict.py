

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stack_info_dict import StackInfoDict


class TaskInfoDict(UniversalBaseModel):
    txt: str
    type: str
    done: bool
    cancelled: bool
    stack: typing.List[StackInfoDict]
    exception: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
