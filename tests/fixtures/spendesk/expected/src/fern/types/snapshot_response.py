

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payable import Payable


class SnapshotResponse(UniversalBaseModel):
    snapshot_id: typing.Optional[str] = None
    status: typing.Optional[str] = None
    data: typing.Optional[typing.List[Payable]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
