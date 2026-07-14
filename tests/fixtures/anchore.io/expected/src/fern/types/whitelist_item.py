

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WhitelistItem(UniversalBaseModel):
    """
    Identifies a specific gate and trigger match from a policy against an image and indicates it should be ignored in final policy decisions
    """

    expires_on: typing.Optional[dt.datetime] = None
    gate: str
    id: typing.Optional[str] = None
    trigger_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
