

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_result_line import QueryResultLine


class QueryResult(UniversalBaseModel):
    total_number_of_patients: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalNumberOfPatients"),
        pydantic.Field(alias="totalNumberOfPatients"),
    ] = None
    query_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="queryId"), pydantic.Field(alias="queryId")
    ] = None
    result_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[QueryResultLine]],
        FieldMetadata(alias="resultLines"),
        pydantic.Field(alias="resultLines"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
