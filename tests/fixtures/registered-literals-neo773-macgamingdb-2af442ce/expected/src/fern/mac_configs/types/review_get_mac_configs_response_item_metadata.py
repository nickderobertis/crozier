

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ReviewGetMacConfigsResponseItemMetadata(UniversalBaseModel):
    family: str
    model: str
    identifier: str
    chip: str
    chip_variant: typing_extensions.Annotated[
        str, FieldMetadata(alias="chipVariant"), pydantic.Field(alias="chipVariant")
    ]
    cpu_cores: typing_extensions.Annotated[float, FieldMetadata(alias="cpuCores"), pydantic.Field(alias="cpuCores")]
    gpu_cores: typing_extensions.Annotated[float, FieldMetadata(alias="gpuCores"), pydantic.Field(alias="gpuCores")]
    ram: float
    year: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
