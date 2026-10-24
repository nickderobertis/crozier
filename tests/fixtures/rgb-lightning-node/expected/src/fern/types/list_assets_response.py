

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_cfa import AssetCfa
from .asset_ifa import AssetIfa
from .asset_nia import AssetNia
from .asset_uda import AssetUda


class ListAssetsResponse(UniversalBaseModel):
    nia: typing.Optional[typing.List[AssetNia]] = None
    uda: typing.Optional[typing.List[AssetUda]] = None
    cfa: typing.Optional[typing.List[AssetCfa]] = None
    ifa: typing.Optional[typing.List[AssetIfa]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
