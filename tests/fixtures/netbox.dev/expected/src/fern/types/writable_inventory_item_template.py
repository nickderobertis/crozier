

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WritableInventoryItemTemplate(UniversalBaseModel):
    depth: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="_depth"), pydantic.Field(alias="_depth")
    ] = None
    component: typing.Optional[typing.Dict[str, typing.Any]] = None
    component_id: typing.Optional[int] = None
    component_type: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    device_type: int
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    manufacturer: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    parent: typing.Optional[int] = None
    part_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Manufacturer-assigned part identifier
    """

    role: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
