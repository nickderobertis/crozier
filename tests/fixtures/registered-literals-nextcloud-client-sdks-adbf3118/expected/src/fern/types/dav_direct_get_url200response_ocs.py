

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dav_direct_get_url200response_ocs_data import DavDirectGetUrl200ResponseOcsData
from .ocs_meta import OcsMeta


class DavDirectGetUrl200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: DavDirectGetUrl200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
