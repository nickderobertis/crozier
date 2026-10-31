

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskGet(UniversalBaseModel):
    task_id: str
    task_name: typing.Optional[str] = None
    status_href: str
    abort_href: str
    result_href: typing.Optional[str] = None
    stream_href: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
