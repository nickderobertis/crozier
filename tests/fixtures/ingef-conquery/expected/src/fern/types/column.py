

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_type import ColumnType
from .secondary_id_id import SecondaryIdId


class Column(UniversalBaseModel):
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None
    type: typing.Optional[ColumnType] = None
    description: typing.Optional[str] = None
    min_suffix_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minSuffixLength"), pydantic.Field(alias="minSuffixLength")
    ] = None
    generate_suffixes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="generateSuffixes"), pydantic.Field(alias="generateSuffixes")
    ] = None
    search_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="searchDisabled"), pydantic.Field(alias="searchDisabled")
    ] = None
    secondary_id: typing_extensions.Annotated[
        typing.Optional[SecondaryIdId], FieldMetadata(alias="secondaryId"), pydantic.Field(alias="secondaryId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
