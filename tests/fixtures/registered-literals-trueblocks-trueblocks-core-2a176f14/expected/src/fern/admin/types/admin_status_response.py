

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_status_response_data_item import AdminStatusResponseDataItem


class AdminStatusResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AdminStatusResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/admin/#cacheitem">CacheItem</a>, <a href="/data-model/admin/#chain">Chain</a> or <a href="/data-model/admin/#status">Status</a> data. Corresponds to the <a href="/chifra/admin/#chifra-status">chifra status</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
