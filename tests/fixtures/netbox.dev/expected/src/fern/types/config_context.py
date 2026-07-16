

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_cluster import NestedCluster
from .nested_cluster_group import NestedClusterGroup
from .nested_cluster_type import NestedClusterType
from .nested_device_role import NestedDeviceRole
from .nested_device_type import NestedDeviceType
from .nested_location import NestedLocation
from .nested_platform import NestedPlatform
from .nested_region import NestedRegion
from .nested_site import NestedSite
from .nested_site_group import NestedSiteGroup
from .nested_tenant import NestedTenant
from .nested_tenant_group import NestedTenantGroup


class ConfigContext(UniversalBaseModel):
    cluster_groups: typing.Optional[typing.List[NestedClusterGroup]] = None
    cluster_types: typing.Optional[typing.List[NestedClusterType]] = None
    clusters: typing.Optional[typing.List[typing.Optional[NestedCluster]]] = None
    created: typing.Optional[dt.datetime] = None
    data: typing.Dict[str, typing.Optional[typing.Any]]
    description: typing.Optional[str] = None
    device_types: typing.Optional[typing.List[NestedDeviceType]] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_active: typing.Optional[bool] = None
    last_updated: typing.Optional[dt.datetime] = None
    locations: typing.Optional[typing.List[typing.Optional[NestedLocation]]] = None
    name: str
    platforms: typing.Optional[typing.List[typing.Optional[NestedPlatform]]] = None
    regions: typing.Optional[typing.List[typing.Optional[NestedRegion]]] = None
    roles: typing.Optional[typing.List[NestedDeviceRole]] = None
    site_groups: typing.Optional[typing.List[typing.Optional[NestedSiteGroup]]] = None
    sites: typing.Optional[typing.List[typing.Optional[NestedSite]]] = None
    tags: typing.Optional[typing.List[str]] = None
    tenant_groups: typing.Optional[typing.List[NestedTenantGroup]] = None
    tenants: typing.Optional[typing.List[typing.Optional[NestedTenant]]] = None
    url: typing.Optional[str] = None
    weight: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
