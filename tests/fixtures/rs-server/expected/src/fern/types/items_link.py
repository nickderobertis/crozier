

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .items_link_method import ItemsLinkMethod
from .items_link_rel import ItemsLinkRel
from .items_link_type import ItemsLinkType


class ItemsLink(UniversalBaseModel):
    href: str
    rel: ItemsLinkRel
    type: typing.Optional[ItemsLinkType] = None
    title: typing.Optional[str] = None
    method: typing.Optional[ItemsLinkMethod] = None
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
