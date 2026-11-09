

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .disk_usage_data_item import DiskUsageDataItem
from .disk_usage_notes import DiskUsageNotes


class DiskUsage(UniversalBaseModel):
    data: typing.Optional[typing.List[DiskUsageDataItem]] = pydantic.Field(default=None)
    """
    List of filesystem information
    """

    notes: typing.Optional[DiskUsageNotes] = pydantic.Field(default=None)
    """
    Additional notes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
