

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag


class WritableVrf(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    enforce_unique: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Prevent duplicate prefixes/IP addresses within this VRF
    """

    export_targets: typing.Optional[typing.List[int]] = None
    id: typing.Optional[int] = None
    import_targets: typing.Optional[typing.List[int]] = None
    ipaddress_count: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    prefix_count: typing.Optional[int] = None
    rd: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique route distinguisher (as defined in RFC 4364)
    """

    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
