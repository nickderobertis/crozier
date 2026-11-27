

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .initial_table import InitialTable


class EntryCreateInitialTablesArray(UniversalBaseModel):
    initial_tables: typing_extensions.Annotated[
        typing.Optional[typing.List[InitialTable]],
        FieldMetadata(alias="initialTables"),
        pydantic.Field(alias="initialTables"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
