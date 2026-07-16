

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyArrangementRegionFilterDefinition(UniversalBaseModel):
    arrangement_index_by_stat_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="arrangementIndexByStatValue"),
        pydantic.Field(alias="arrangementIndexByStatValue"),
    ] = None
    art_arrangement_region_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="artArrangementRegionHash"),
        pydantic.Field(alias="artArrangementRegionHash"),
    ] = None
    art_arrangement_region_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="artArrangementRegionIndex"),
        pydantic.Field(alias="artArrangementRegionIndex"),
    ] = None
    stat_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="statHash"), pydantic.Field(alias="statHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
