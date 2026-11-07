

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dav_direct_get_url200response_ocs import DavDirectGetUrl200ResponseOcs


class DavDirectGetUrl200Response(UniversalBaseModel):
    ocs: DavDirectGetUrl200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
