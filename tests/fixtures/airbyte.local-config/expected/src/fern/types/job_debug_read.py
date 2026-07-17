

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_definition_read import DestinationDefinitionRead
from .job_config_type import JobConfigType
from .job_id import JobId
from .job_status import JobStatus
from .source_definition_read import SourceDefinitionRead


class JobDebugRead(UniversalBaseModel):
    airbyte_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="airbyteVersion"), pydantic.Field(alias="airbyteVersion")
    ]
    config_id: typing_extensions.Annotated[str, FieldMetadata(alias="configId"), pydantic.Field(alias="configId")]
    config_type: typing_extensions.Annotated[
        JobConfigType, FieldMetadata(alias="configType"), pydantic.Field(alias="configType")
    ]
    destination_definition: typing_extensions.Annotated[
        DestinationDefinitionRead,
        FieldMetadata(alias="destinationDefinition"),
        pydantic.Field(alias="destinationDefinition"),
    ]
    id: JobId
    source_definition: typing_extensions.Annotated[
        SourceDefinitionRead, FieldMetadata(alias="sourceDefinition"), pydantic.Field(alias="sourceDefinition")
    ]
    status: JobStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
