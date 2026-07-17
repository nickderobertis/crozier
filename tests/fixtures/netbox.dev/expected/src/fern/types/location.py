

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location_status import LocationStatus
from .nested_location import NestedLocation
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class Location(UniversalBaseModel):
    depth: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="_depth"), pydantic.Field(alias="_depth")
    ] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    parent: typing.Optional[NestedLocation] = None
    rack_count: typing.Optional[int] = None
    site: typing.Optional[NestedSite] = None
    slug: str
    status: typing.Optional[LocationStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
