

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .prebuild_mode import PrebuildMode


class Pool(UniversalBaseModel):
    pool_type: typing_extensions.Annotated[
        typing.Optional[PrebuildMode], FieldMetadata(alias="poolType"), pydantic.Field(alias="poolType")
    ] = None
    sku_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="skuName"), pydantic.Field(alias="skuName")
    ] = None
    target_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="targetCount"), pydantic.Field(alias="targetCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
