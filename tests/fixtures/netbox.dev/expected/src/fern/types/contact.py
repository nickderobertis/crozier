

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_contact_group import NestedContactGroup
from .nested_tag import NestedTag


class Contact(UniversalBaseModel):
    address: typing.Optional[str] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    email: typing.Optional[str] = None
    group: typing.Optional[NestedContactGroup] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    link: typing.Optional[str] = None
    name: str
    phone: typing.Optional[str] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
