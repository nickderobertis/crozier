

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord(UniversalBaseModel):
    client_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ClientCount"), pydantic.Field(alias="ClientCount")
    ] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ErrorCode"), pydantic.Field(alias="ErrorCode")
    ] = None
    long_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LongDescription"), pydantic.Field(alias="LongDescription")
    ] = None
    short_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShortDescription"), pydantic.Field(alias="ShortDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
