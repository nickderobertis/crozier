

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .report_col_part_def import ReportColPartDef


class ReportColDef(UniversalBaseModel):
    full_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullPath"), pydantic.Field(alias="fullPath")
    ] = None
    parts: typing.Optional[typing.List[ReportColPartDef]] = None
    root_entity_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rootEntityClass"), pydantic.Field(alias="rootEntityClass")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
