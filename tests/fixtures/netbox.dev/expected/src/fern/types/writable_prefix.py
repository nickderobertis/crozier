

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_tag import NestedTag
from .writable_prefix_status import WritablePrefixStatus


class WritablePrefix(UniversalBaseModel):
    depth: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="_depth")] = None
    children: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    family: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_pool: typing.Optional[bool] = pydantic.Field(default=None)
    """
    All IP addresses within this prefix are considered usable
    """

    last_updated: typing.Optional[dt.datetime] = None
    mark_utilized: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Treat as 100% utilized
    """

    prefix: str = pydantic.Field()
    """
    IPv4 or IPv6 network with mask
    """

    role: typing.Optional[int] = pydantic.Field(default=None)
    """
    The primary function of this prefix
    """

    site: typing.Optional[int] = None
    status: typing.Optional[WritablePrefixStatus] = pydantic.Field(default=None)
    """
    Operational status of this prefix
    """

    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vlan: typing.Optional[int] = None
    vrf: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
