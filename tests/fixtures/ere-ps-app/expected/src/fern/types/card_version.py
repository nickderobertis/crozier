

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .version_info_type import VersionInfoType


class CardVersion(UniversalBaseModel):
    cos_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType], FieldMetadata(alias="cosVersion"), pydantic.Field(alias="cosVersion")
    ] = None
    object_system_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType],
        FieldMetadata(alias="objectSystemVersion"),
        pydantic.Field(alias="objectSystemVersion"),
    ] = None
    card_pt_pers_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType],
        FieldMetadata(alias="cardPTPersVersion"),
        pydantic.Field(alias="cardPTPersVersion"),
    ] = None
    data_structure_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType],
        FieldMetadata(alias="dataStructureVersion"),
        pydantic.Field(alias="dataStructureVersion"),
    ] = None
    logging_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType], FieldMetadata(alias="loggingVersion"), pydantic.Field(alias="loggingVersion")
    ] = None
    atr_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType], FieldMetadata(alias="atrVersion"), pydantic.Field(alias="atrVersion")
    ] = None
    gdo_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType], FieldMetadata(alias="gdoVersion"), pydantic.Field(alias="gdoVersion")
    ] = None
    key_info_version: typing_extensions.Annotated[
        typing.Optional[VersionInfoType], FieldMetadata(alias="keyInfoVersion"), pydantic.Field(alias="keyInfoVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
