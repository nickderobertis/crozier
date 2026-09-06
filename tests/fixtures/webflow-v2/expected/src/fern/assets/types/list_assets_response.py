

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_assets_response_assets_item import ListAssetsResponseAssetsItem
from .list_assets_response_pagination import ListAssetsResponsePagination


class ListAssetsResponse(UniversalBaseModel):
    """
    A list of assets
    """

    assets: typing.List[ListAssetsResponseAssetsItem]
    pagination: ListAssetsResponsePagination = pydantic.Field()
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
