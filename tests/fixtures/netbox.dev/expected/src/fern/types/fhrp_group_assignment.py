

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_fhrp_group import NestedFhrpGroup


class FhrpGroupAssignment(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    group: NestedFhrpGroup
    id: typing.Optional[int] = None
    interface: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    interface_id: int
    interface_type: str
    last_updated: typing.Optional[dt.datetime] = None
    priority: int
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
