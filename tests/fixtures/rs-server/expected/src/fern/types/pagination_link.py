

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_link_method import PaginationLinkMethod
from .pagination_link_rel import PaginationLinkRel
from .pagination_link_type import PaginationLinkType


class PaginationLink(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md#pagination
    """

    href: str
    rel: PaginationLinkRel
    type: typing.Optional[PaginationLinkType] = None
    title: typing.Optional[str] = None
    method: typing.Optional[PaginationLinkMethod] = None
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
