

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_location import NestedLocation
from .nested_rack_role import NestedRackRole
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .rack_outer_unit import RackOuterUnit
from .rack_status import RackStatus
from .rack_type import RackType
from .rack_weight_unit import RackWeightUnit
from .rack_width import RackWidth


class Rack(UniversalBaseModel):
    asset_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique tag used to identify this rack
    """

    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    desc_units: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Units are numbered top-to-bottom
    """

    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    facility_id: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    location: typing.Optional[NestedLocation] = None
    max_weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum load capacity for the rack
    """

    mounting_depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum depth of a mounted device, in millimeters. For four-post racks, this is the distance between the front and rear rails.
    """

    name: str
    outer_depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Outer dimension of rack (depth)
    """

    outer_unit: typing.Optional[RackOuterUnit] = None
    outer_width: typing.Optional[int] = pydantic.Field(default=None)
    """
    Outer dimension of rack (width)
    """

    powerfeed_count: typing.Optional[int] = None
    role: typing.Optional[NestedRackRole] = None
    serial: typing.Optional[str] = None
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[RackStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    type: typing.Optional[RackType] = None
    u_height: typing.Optional[int] = pydantic.Field(default=None)
    """
    Height in rack units
    """

    url: typing.Optional[str] = None
    weight: typing.Optional[float] = None
    weight_unit: typing.Optional[RackWeightUnit] = None
    width: typing.Optional[RackWidth] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
