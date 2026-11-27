

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archive_record import ArchiveRecord


class FieldSummary(UniversalBaseModel):
    archive_record: typing_extensions.Annotated[
        typing.Optional[ArchiveRecord], FieldMetadata(alias="archiveRecord"), pydantic.Field(alias="archiveRecord")
    ] = None
    decimal_precision: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="decimalPrecision"), pydantic.Field(alias="decimalPrecision")
    ] = None
    dropdown_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dropdownId"), pydantic.Field(alias="dropdownId")
    ] = None
    id: typing.Optional[str] = None
    is_computed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isComputed"), pydantic.Field(alias="isComputed")
    ] = None
    is_converted_from_link: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isConvertedFromLink"), pydantic.Field(alias="isConvertedFromLink")
    ] = None
    is_integration: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isIntegration"), pydantic.Field(alias="isIntegration")
    ] = None
    is_single_link: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isSingleLink"), pydantic.Field(alias="isSingleLink")
    ] = None
    is_snapshot: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isSnapshot"), pydantic.Field(alias="isSnapshot")
    ] = None
    is_uneditable: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isUneditable"), pydantic.Field(alias="isUneditable")
    ] = None
    legal_text_dropdown_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="legalTextDropdownId"), pydantic.Field(alias="legalTextDropdownId")
    ] = None
    link: typing.Optional[typing.Dict[str, typing.Any]] = None
    numeric_max: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="numericMax"), pydantic.Field(alias="numericMax")
    ] = None
    numeric_min: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="numericMin"), pydantic.Field(alias="numericMin")
    ] = None
    strict_selector: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="strictSelector"), pydantic.Field(alias="strictSelector")
    ] = None
    system_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="systemName"), pydantic.Field(alias="systemName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
