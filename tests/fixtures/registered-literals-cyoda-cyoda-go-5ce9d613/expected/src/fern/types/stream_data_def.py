

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_condition import AbstractCondition
from .report_alias_def import ReportAliasDef
from .report_col_def import ReportColDef
from .report_column import ReportColumn


class StreamDataDef(UniversalBaseModel):
    range_condition: typing_extensions.Annotated[
        typing.Optional[AbstractCondition],
        FieldMetadata(alias="rangeCondition"),
        pydantic.Field(alias="rangeCondition"),
    ] = None
    range_order: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rangeOrder"), pydantic.Field(alias="rangeOrder")
    ] = None
    condition: typing.Optional[AbstractCondition] = None
    columns: typing.Optional[typing.List[ReportColumn]] = None
    col_defs: typing_extensions.Annotated[
        typing.Optional[typing.List[ReportColDef]], FieldMetadata(alias="colDefs"), pydantic.Field(alias="colDefs")
    ] = None
    alias_defs: typing_extensions.Annotated[
        typing.Optional[typing.List[ReportAliasDef]],
        FieldMetadata(alias="aliasDefs"),
        pydantic.Field(alias="aliasDefs"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
