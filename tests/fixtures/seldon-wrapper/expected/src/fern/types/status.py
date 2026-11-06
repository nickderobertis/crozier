

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .status_status_flag import StatusStatusFlag


class Status(UniversalBaseModel):
    code: typing.Optional[int] = None
    info: typing.Optional[str] = None
    reason: typing.Optional[str] = None
    status: typing.Optional[StatusStatusFlag] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
