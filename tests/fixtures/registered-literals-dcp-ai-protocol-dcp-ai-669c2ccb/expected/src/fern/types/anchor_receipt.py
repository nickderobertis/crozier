

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnchorReceipt(UniversalBaseModel):
    anchored: typing.Optional[bool] = None
    chain: typing.Optional[str] = None
    tx_hash: typing.Optional[str] = None
    bundle_hash: typing.Optional[str] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
