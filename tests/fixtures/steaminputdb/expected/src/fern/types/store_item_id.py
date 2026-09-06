

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemId(UniversalBaseModel):
    appid: typing.Optional[int] = None
    bundleid: typing.Optional[int] = None
    creatorid: typing.Optional[int] = None
    hubcategoryid: typing.Optional[int] = None
    packageid: typing.Optional[int] = None
    tagid: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
