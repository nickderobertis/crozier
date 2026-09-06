

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettingMultiSourceInteger(UniversalBaseModel):
    configuration_source: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="configurationSource"), pydantic.Field(alias="configurationSource")
    ] = None
    database_source: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="databaseSource"), pydantic.Field(alias="databaseSource")
    ] = None
    effective_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="effectiveValue"), pydantic.Field(alias="effectiveValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
