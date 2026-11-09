

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_dfu_history_current import DeviceDfuHistoryCurrent
from .device_dfu_state_machine import DeviceDfuStateMachine


class DeviceDfuHistory(UniversalBaseModel):
    current: typing.Optional[DeviceDfuHistoryCurrent] = pydantic.Field(default=None)
    """
    Description of the current firmware
    """

    device_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device UID
    """

    history: typing.Optional[typing.List[DeviceDfuStateMachine]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
