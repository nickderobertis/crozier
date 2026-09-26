

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KmcVmstatGetResponseItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    used_chunks: typing.Optional[int] = None
    huge_pages: typing.Optional[int] = None
    used_slabs: typing.Optional[int] = None
    used_slabs_size: typing.Optional[float] = None
    empty_slabs: typing.Optional[int] = None
    allocated_slabs: typing.Optional[int] = None
    free_slabs: typing.Optional[int] = None
    item_size: typing.Optional[int] = None
    item_alignment: typing.Optional[int] = None
    item_aligned_size: typing.Optional[int] = None
    total_items: typing.Optional[int] = None
    used_items: typing.Optional[int] = None
    allocations: typing.Optional[int] = None
    deallocations: typing.Optional[int] = None
    huge: typing.Optional[bool] = None
    packed: typing.Optional[bool] = None
    hardware_cache_aligned: typing.Optional[bool] = None
    descriptor_convertible: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
