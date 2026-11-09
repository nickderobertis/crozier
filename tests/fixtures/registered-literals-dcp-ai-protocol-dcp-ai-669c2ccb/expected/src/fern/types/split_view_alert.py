

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .split_view_alert_type import SplitViewAlertType


class SplitViewAlert(UniversalBaseModel):
    type: SplitViewAlertType
    peer_id: typing.Optional[str] = None
    peer_log_id: typing.Optional[str] = None
    local_root: str
    peer_root: str
    tree_size: int
    detected_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
