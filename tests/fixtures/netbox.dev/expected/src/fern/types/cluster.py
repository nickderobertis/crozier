

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cluster_status import ClusterStatus
from .nested_cluster_group import NestedClusterGroup
from .nested_cluster_type import NestedClusterType
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class Cluster(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    group: typing.Optional[NestedClusterGroup] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[ClusterStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    type: NestedClusterType
    url: typing.Optional[str] = None
    virtualmachine_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
