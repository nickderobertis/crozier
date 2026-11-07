

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .report_alias_path_def import ReportAliasPathDef


class ReportAliasDef(UniversalBaseModel):
    name: typing.Optional[str] = None
    alias_paths: typing_extensions.Annotated[
        typing.Optional[typing.List[ReportAliasPathDef]],
        FieldMetadata(alias="aliasPaths"),
        pydantic.Field(alias="aliasPaths"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
