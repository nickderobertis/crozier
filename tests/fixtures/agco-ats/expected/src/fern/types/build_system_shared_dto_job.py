

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_job_activity import BuildSystemSharedDtoJobActivity
from .build_system_shared_dto_parameter import BuildSystemSharedDtoParameter


class BuildSystemSharedDtoJob(UniversalBaseModel):
    """
    A DTO for an IJob
    """

    activities: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoJobActivity]],
        FieldMetadata(alias="Activities"),
        pydantic.Field(alias="Activities", description="The activities which are performed for the job"),
    ] = None
    """
    The activities which are performed for the job
    """

    deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Deleted"),
        pydantic.Field(alias="Deleted", description="Indicates if the job has been deleted."),
    ] = None
    """
    Indicates if the job has been deleted.
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobID"),
        pydantic.Field(alias="JobID", description="The ID of the job"),
    ] = None
    """
    The ID of the job
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the job"),
    ] = None
    """
    The name of the job
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameter]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="The parameters for the job"),
    ] = None
    """
    The parameters for the job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
