

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WritableConfigContext(UniversalBaseModel):
    cluster_groups: typing.Optional[typing.List[int]] = None
    cluster_types: typing.Optional[typing.List[int]] = None
    clusters: typing.Optional[typing.List[int]] = None
    created: typing.Optional[dt.datetime] = None
    data: typing.Dict[str, typing.Optional[typing.Any]]
    description: typing.Optional[str] = None
    device_types: typing.Optional[typing.List[int]] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_active: typing.Optional[bool] = None
    last_updated: typing.Optional[dt.datetime] = None
    locations: typing.Optional[typing.List[int]] = None
    name: str
    platforms: typing.Optional[typing.List[int]] = None
    regions: typing.Optional[typing.List[int]] = None
    roles: typing.Optional[typing.List[int]] = None
    site_groups: typing.Optional[typing.List[int]] = None
    sites: typing.Optional[typing.List[int]] = None
    tags: typing.Optional[typing.List[str]] = None
    tenant_groups: typing.Optional[typing.List[int]] = None
    tenants: typing.Optional[typing.List[int]] = None
    url: typing.Optional[str] = None
    weight: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
