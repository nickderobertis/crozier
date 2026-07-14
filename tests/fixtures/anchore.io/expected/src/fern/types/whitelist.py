

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .whitelist_item import WhitelistItem


class Whitelist(UniversalBaseModel):
    """
    A collection of whitelist items to match a policy evaluation against.
    """

    comment: typing.Optional[str] = None
    id: str
    items: typing.Optional[typing.List[WhitelistItem]] = None
    name: typing.Optional[str] = None
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
