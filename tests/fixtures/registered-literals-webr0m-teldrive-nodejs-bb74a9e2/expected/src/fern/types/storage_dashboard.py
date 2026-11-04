

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_category_statistics import FileCategoryStatistics
from .storage_activity import StorageActivity
from .storage_channel_statistic import StorageChannelStatistic
from .storage_cleanup_statistics import StorageCleanupStatistics
from .storage_growth_point import StorageGrowthPoint
from .storage_summary import StorageSummary


class StorageDashboard(UniversalBaseModel):
    summary: StorageSummary
    growth: typing.List[StorageGrowthPoint]
    categories: typing.List[FileCategoryStatistics]
    channels: typing.List[StorageChannelStatistic]
    cleanup: StorageCleanupStatistics
    activity: typing.List[StorageActivity]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
