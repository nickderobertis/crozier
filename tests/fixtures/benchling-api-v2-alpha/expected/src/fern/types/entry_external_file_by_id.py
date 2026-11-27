

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_external_file import EntryExternalFile


class EntryExternalFileById(UniversalBaseModel):
    external_file: typing_extensions.Annotated[
        typing.Optional[EntryExternalFile], FieldMetadata(alias="externalFile"), pydantic.Field(alias="externalFile")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
