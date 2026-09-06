

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BookImportDto(UniversalBaseModel):
    destination_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="destinationName"), pydantic.Field(alias="destinationName")
    ] = None
    series_id: typing_extensions.Annotated[str, FieldMetadata(alias="seriesId"), pydantic.Field(alias="seriesId")]
    source_file: typing_extensions.Annotated[str, FieldMetadata(alias="sourceFile"), pydantic.Field(alias="sourceFile")]
    upgrade_book_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="upgradeBookId"), pydantic.Field(alias="upgradeBookId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
