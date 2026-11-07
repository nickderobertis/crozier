

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageUsageDetail(UniversalBaseModel):
    size: typing.Optional[int] = None
    size_in_kb: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sizeInKB"), pydantic.Field(alias="sizeInKB")
    ] = None
    sku: typing.Optional[str] = None
    usage: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
