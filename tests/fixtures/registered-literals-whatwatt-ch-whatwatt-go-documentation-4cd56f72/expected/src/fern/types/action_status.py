

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ActionStatus(UniversalBaseModel):
    action_id: typing.Optional[str] = None
    id: typing.Optional[int] = None
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP status or negative codes for Modbus/connection; -1 while running
    """

    exe_time: typing.Optional[float] = pydantic.Field(default=None)
    """
    Seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
