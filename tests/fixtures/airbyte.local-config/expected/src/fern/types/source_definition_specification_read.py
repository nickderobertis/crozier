

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .advanced_auth import AdvancedAuth
from .source_auth_specification import SourceAuthSpecification
from .source_definition_id import SourceDefinitionId
from .source_definition_specification import SourceDefinitionSpecification
from .synchronous_job_read import SynchronousJobRead


class SourceDefinitionSpecificationRead(UniversalBaseModel):
    advanced_auth: typing_extensions.Annotated[typing.Optional[AdvancedAuth], FieldMetadata(alias="advancedAuth")] = (
        None
    )
    auth_specification: typing_extensions.Annotated[
        typing.Optional[SourceAuthSpecification], FieldMetadata(alias="authSpecification")
    ] = None
    connection_specification: typing_extensions.Annotated[
        typing.Optional[SourceDefinitionSpecification], FieldMetadata(alias="connectionSpecification")
    ] = None
    documentation_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="documentationUrl")] = None
    job_info: typing_extensions.Annotated[SynchronousJobRead, FieldMetadata(alias="jobInfo")]
    source_definition_id: typing_extensions.Annotated[SourceDefinitionId, FieldMetadata(alias="sourceDefinitionId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
