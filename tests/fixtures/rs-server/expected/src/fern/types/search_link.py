

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_link_method import SearchLinkMethod
from .search_link_rel import SearchLinkRel
from .search_link_type import SearchLinkType


class SearchLink(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/item-search#link-relations
    """

    href: str
    rel: SearchLinkRel
    type: typing.Optional[SearchLinkType] = None
    title: typing.Optional[str] = None
    method: typing.Optional[SearchLinkMethod] = None
    headers: typing.Optional[typing.Dict[str, typing.Any]] = None
    body: typing.Optional[typing.Dict[str, typing.Any]] = None
    merge: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
