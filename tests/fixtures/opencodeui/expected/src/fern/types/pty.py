

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pty_status import PtyStatus


class Pty(UniversalBaseModel):
    id: str
    title: str
    command: str
    args: typing.List[str]
    cwd: str
    status: PtyStatus
    pid: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
