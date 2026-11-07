

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_query_list_entry_ccdl import DataQueryListEntryCcdl
from .data_query_list_entry_data_extraction import DataQueryListEntryDataExtraction


class DataQueryListEntry(UniversalBaseModel):
    id: int
    label: str
    comment: typing.Optional[str] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    result_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="resultSize"), pydantic.Field(alias="resultSize")
    ] = None
    ccdl: typing.Optional[DataQueryListEntryCcdl] = None
    data_extraction: typing_extensions.Annotated[
        typing.Optional[DataQueryListEntryDataExtraction],
        FieldMetadata(alias="dataExtraction"),
        pydantic.Field(alias="dataExtraction"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
