

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_basic_info_creator_home_link import StoreItemBasicInfoCreatorHomeLink


class StoreItemBasicInfo(UniversalBaseModel):
    capsule_headline: typing.Optional[str] = None
    developers: typing.Optional[typing.List[StoreItemBasicInfoCreatorHomeLink]] = None
    franchises: typing.Optional[typing.List[StoreItemBasicInfoCreatorHomeLink]] = None
    publishers: typing.Optional[typing.List[StoreItemBasicInfoCreatorHomeLink]] = None
    short_description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
