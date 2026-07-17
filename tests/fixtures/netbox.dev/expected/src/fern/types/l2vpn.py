

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .l2vpn_type import L2VpnType
from .nested_route_target import NestedRouteTarget
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class L2Vpn(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    export_targets: typing.Optional[typing.List[NestedRouteTarget]] = None
    id: typing.Optional[int] = None
    identifier: typing.Optional[int] = None
    import_targets: typing.Optional[typing.List[NestedRouteTarget]] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    slug: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    type: typing.Optional[L2VpnType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
