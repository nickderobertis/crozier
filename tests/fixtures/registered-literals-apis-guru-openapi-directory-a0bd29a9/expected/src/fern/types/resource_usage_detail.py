

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compute_usage_detail import ComputeUsageDetail
from .storage_usage_detail import StorageUsageDetail


class ResourceUsageDetail(UniversalBaseModel):
    compute: typing.Optional[typing.List[ComputeUsageDetail]] = None
    storage: typing.Optional[typing.List[StorageUsageDetail]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
