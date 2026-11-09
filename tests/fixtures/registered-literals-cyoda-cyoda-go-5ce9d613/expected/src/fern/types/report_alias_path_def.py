

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alias_mapper_parameters import AliasMapperParameters
from .report_col_def import ReportColDef


class ReportAliasPathDef(UniversalBaseModel):
    col_def: typing_extensions.Annotated[
        typing.Optional[ReportColDef], FieldMetadata(alias="colDef"), pydantic.Field(alias="colDef")
    ] = None
    mapper_parameters: typing_extensions.Annotated[
        typing.Optional[AliasMapperParameters],
        FieldMetadata(alias="mapperParameters"),
        pydantic.Field(alias="mapperParameters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
