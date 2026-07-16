

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .advanced_auth import AdvancedAuth
from .destination_auth_specification import DestinationAuthSpecification
from .destination_definition_id import DestinationDefinitionId
from .destination_definition_specification import DestinationDefinitionSpecification
from .destination_sync_mode import DestinationSyncMode
from .synchronous_job_read import SynchronousJobRead


class DestinationDefinitionSpecificationRead(UniversalBaseModel):
    advanced_auth: typing_extensions.Annotated[
        typing.Optional[AdvancedAuth], FieldMetadata(alias="advancedAuth"), pydantic.Field(alias="advancedAuth")
    ] = None
    auth_specification: typing_extensions.Annotated[
        typing.Optional[DestinationAuthSpecification],
        FieldMetadata(alias="authSpecification"),
        pydantic.Field(alias="authSpecification"),
    ] = None
    connection_specification: typing_extensions.Annotated[
        typing.Optional[DestinationDefinitionSpecification],
        FieldMetadata(alias="connectionSpecification"),
        pydantic.Field(alias="connectionSpecification"),
    ] = None
    destination_definition_id: typing_extensions.Annotated[
        DestinationDefinitionId,
        FieldMetadata(alias="destinationDefinitionId"),
        pydantic.Field(alias="destinationDefinitionId"),
    ]
    documentation_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentationUrl"), pydantic.Field(alias="documentationUrl")
    ] = None
    job_info: typing_extensions.Annotated[
        SynchronousJobRead, FieldMetadata(alias="jobInfo"), pydantic.Field(alias="jobInfo")
    ]
    supported_destination_sync_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinationSyncMode]],
        FieldMetadata(alias="supportedDestinationSyncModes"),
        pydantic.Field(alias="supportedDestinationSyncModes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
