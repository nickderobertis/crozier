

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_role import NestedRole
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_vlan import NestedVlan
from .nested_vrf import NestedVrf
from .prefix_family import PrefixFamily
from .prefix_status import PrefixStatus


class Prefix(UniversalBaseModel):
    depth: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="_depth")] = None
    children: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    family: typing.Optional[PrefixFamily] = None
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

    role: typing.Optional[NestedRole] = None
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[PrefixStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vlan: typing.Optional[NestedVlan] = None
    vrf: typing.Optional[NestedVrf] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
