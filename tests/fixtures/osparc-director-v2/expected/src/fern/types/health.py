

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .healthcheck_result import HealthcheckResult
from .models_library_generated_models_docker_rest_api_status import ModelsLibraryGeneratedModelsDockerRestApiStatus


class Health(UniversalBaseModel):
    """
    Health stores information about the container's healthcheck results.
    """

    status: typing_extensions.Annotated[
        typing.Optional[ModelsLibraryGeneratedModelsDockerRestApiStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description='Status is one of `none`, `starting`, `healthy` or `unhealthy`\n\n- "none"      Indicates there is no healthcheck\n- "starting"  Starting indicates that the container is not yet ready\n- "healthy"   Healthy indicates that the container is running correctly\n- "unhealthy" Unhealthy indicates that the container has a problem',
        ),
    ] = None
    """
    Status is one of `none`, `starting`, `healthy` or `unhealthy`
    
    - "none"      Indicates there is no healthcheck
    - "starting"  Starting indicates that the container is not yet ready
    - "healthy"   Healthy indicates that the container is running correctly
    - "unhealthy" Unhealthy indicates that the container has a problem
    """

    failing_streak: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="FailingStreak"),
        pydantic.Field(alias="FailingStreak", description="FailingStreak is the number of consecutive failures"),
    ] = None
    """
    FailingStreak is the number of consecutive failures
    """

    log: typing_extensions.Annotated[
        typing.Optional[typing.List[HealthcheckResult]],
        FieldMetadata(alias="Log"),
        pydantic.Field(alias="Log", description="Log contains the last few results (oldest first)"),
    ] = None
    """
    Log contains the last few results (oldest first)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
