

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_config_type import JobConfigType
from .log_read import LogRead


class SynchronousJobRead(UniversalBaseModel):
    config_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="configId"),
        pydantic.Field(alias="configId", description="only present if a config id was provided."),
    ] = None
    """
    only present if a config id was provided.
    """

    config_type: typing_extensions.Annotated[
        JobConfigType, FieldMetadata(alias="configType"), pydantic.Field(alias="configType")
    ]
    connector_configuration_updated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="connectorConfigurationUpdated"),
        pydantic.Field(alias="connectorConfigurationUpdated"),
    ] = None
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    ended_at: typing_extensions.Annotated[int, FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")]
    id: str
    logs: typing.Optional[LogRead] = None
    succeeded: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
