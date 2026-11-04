

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.warehouse import Warehouse
from .depot_record_contents_item import DepotRecordContentsItem
from .depot_record_status import DepotRecordStatus


class DepotRecord(UniversalBaseModel):
    status: typing.Optional[DepotRecordStatus] = None
    contents: typing.Optional[typing.List[DepotRecordContentsItem]] = None
    warehouse: typing.Optional[Warehouse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
