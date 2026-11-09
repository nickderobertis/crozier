

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .create_span_body import CreateSpanBody
from .ingestion_usage import IngestionUsage
from .map_value import MapValue
from .usage_details import UsageDetails


class CreateGenerationBody(CreateSpanBody):
    completion_start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completionStartTime"),
        pydantic.Field(alias="completionStartTime"),
    ] = None
    model: typing.Optional[str] = None
    model_parameters: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[MapValue]]],
        FieldMetadata(alias="modelParameters"),
        pydantic.Field(alias="modelParameters"),
    ] = None
    usage: typing.Optional[IngestionUsage] = None
    usage_details: typing_extensions.Annotated[
        typing.Optional[UsageDetails], FieldMetadata(alias="usageDetails"), pydantic.Field(alias="usageDetails")
    ] = None
    cost_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[float]]],
        FieldMetadata(alias="costDetails"),
        pydantic.Field(alias="costDetails"),
    ] = None
    prompt_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="promptName"), pydantic.Field(alias="promptName")
    ] = None
    prompt_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="promptVersion"), pydantic.Field(alias="promptVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
