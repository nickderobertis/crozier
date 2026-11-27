

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StructuredTableColumnInfo(UniversalBaseModel):
    column_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="columnId"), pydantic.Field(alias="columnId")
    ] = None
    is_read_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isReadOnly"), pydantic.Field(alias="isReadOnly")
    ] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
