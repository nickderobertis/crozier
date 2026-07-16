

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_device import NestedDevice
from .nested_inventory_item_role import NestedInventoryItemRole
from .nested_manufacturer import NestedManufacturer
from .nested_tag import NestedTag


class InventoryItem(UniversalBaseModel):
    depth: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="_depth"), pydantic.Field(alias="_depth")
    ] = None
    asset_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique tag used to identify this item
    """

    component: typing.Optional[typing.Dict[str, typing.Any]] = None
    component_id: typing.Optional[int] = None
    component_type: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: NestedDevice
    discovered: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This item was automatically discovered
    """

    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    manufacturer: typing.Optional[NestedManufacturer] = None
    name: str
    parent: typing.Optional[int] = None
    part_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Manufacturer-assigned part identifier
    """

    role: typing.Optional[NestedInventoryItemRole] = None
    serial: typing.Optional[str] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
