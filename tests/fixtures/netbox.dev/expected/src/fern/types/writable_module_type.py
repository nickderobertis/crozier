

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_module_type_weight_unit import WritableModuleTypeWeightUnit


class WritableModuleType(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    manufacturer: int
    model: str
    part_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Discrete part number (optional)
    """

    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None
    weight: typing.Optional[float] = None
    weight_unit: typing.Optional[WritableModuleTypeWeightUnit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
