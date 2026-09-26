

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocFormsGet200ResponseFieldsItemTextFlags(UniversalBaseModel):
    read_only: typing_extensions.Annotated[bool, FieldMetadata(alias="readOnly"), pydantic.Field(alias="readOnly")]
    required: bool
    no_export: typing_extensions.Annotated[bool, FieldMetadata(alias="noExport"), pydantic.Field(alias="noExport")]
    raw: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
