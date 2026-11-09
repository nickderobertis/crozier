

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dataset_status import DatasetStatus


class DatasetItem(UniversalBaseModel):
    id: str
    status: DatasetStatus
    input: typing.Optional[typing.Any] = None
    expected_output: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="expectedOutput"), pydantic.Field(alias="expectedOutput")
    ] = None
    metadata: typing.Optional[typing.Any] = None
    source_trace_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceTraceId"), pydantic.Field(alias="sourceTraceId")
    ] = None
    source_observation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceObservationId"), pydantic.Field(alias="sourceObservationId")
    ] = None
    dataset_id: typing_extensions.Annotated[str, FieldMetadata(alias="datasetId"), pydantic.Field(alias="datasetId")]
    dataset_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="datasetName"), pydantic.Field(alias="datasetName")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
