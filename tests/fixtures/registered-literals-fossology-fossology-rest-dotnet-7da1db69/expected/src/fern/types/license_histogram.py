

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LicenseHistogram(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    scanner_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="scannerCount"), pydantic.Field(alias="scannerCount")
    ] = None
    concluded_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="concludedCount"), pydantic.Field(alias="concludedCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
