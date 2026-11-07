

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .records_get_schema_response_record_types_contract import RecordsGetSchemaResponseRecordTypesContract


class RecordsGetSchemaResponseRecordTypes(UniversalBaseModel):
    contract: typing.Optional[RecordsGetSchemaResponseRecordTypesContract] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
