

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .structured_table_column_info import StructuredTableColumnInfo


class StructuredTableApiIdentifiers(UniversalBaseModel):
    api_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiId"), pydantic.Field(alias="apiId")
    ] = None
    columns: typing.Optional[typing.List[StructuredTableColumnInfo]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
