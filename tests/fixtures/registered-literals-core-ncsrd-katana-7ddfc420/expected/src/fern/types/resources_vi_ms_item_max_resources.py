

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResourcesViMsItemMaxResources(UniversalBaseModel):
    cp_us: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="CPUs"), pydantic.Field(alias="CPUs")
    ] = None
    ram: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="RAM"), pydantic.Field(alias="RAM")] = (
        None
    )
    disk: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Disk"), pydantic.Field(alias="Disk")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
