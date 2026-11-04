

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .depot_record_contents_item_size import DepotRecordContentsItemSize


class DepotRecordContentsItem(UniversalBaseModel):
    label: typing.Optional[str] = None
    size: typing.Optional[DepotRecordContentsItemSize] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
