

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partial_item_type import PartialItemType


class PartialItem(UniversalBaseModel):
    """
    Partial STAC Item.
    """

    type: typing.Optional[PartialItemType] = None
    stac_version: typing.Optional[str] = None
    stac_extensions: typing.Optional[typing.List[str]] = None
    id: typing.Optional[str] = None
    geometry: typing.Optional[typing.Dict[str, typing.Any]] = None
    bbox: typing.Optional[typing.List[typing.Any]] = None
    properties: typing.Optional[typing.Dict[str, typing.Any]] = None
    links: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    assets: typing.Optional[typing.Dict[str, typing.Any]] = None
    collection: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
