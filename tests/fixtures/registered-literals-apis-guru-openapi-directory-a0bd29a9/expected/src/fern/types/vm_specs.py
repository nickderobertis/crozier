

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vm_disk_type import VmDiskType


class VmSpecs(UniversalBaseModel):
    disk_type: typing_extensions.Annotated[
        VmDiskType, FieldMetadata(alias="diskType"), pydantic.Field(alias="diskType")
    ]
    image_resource_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="imageResourceId"), pydantic.Field(alias="imageResourceId")
    ]
    size: str
    subnet_resource_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="subnetResourceId"), pydantic.Field(alias="subnetResourceId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
