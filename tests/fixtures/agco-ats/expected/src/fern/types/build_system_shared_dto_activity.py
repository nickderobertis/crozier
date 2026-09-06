

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from .build_system_shared_dto_parameter import BuildSystemSharedDtoParameter


class BuildSystemSharedDtoActivity(UniversalBaseModel):
    """
    A DTO for an IActivity
    """

    activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityID"),
        pydantic.Field(alias="ActivityID", description="The ID of the activity"),
    ] = None
    """
    The ID of the activity
    """

    deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="Deleted"), pydantic.Field(alias="Deleted", description="")
    ] = None
    """
    
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the activity"),
    ] = None
    """
    The name of the activity
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameter]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="The parameters for this activity"),
    ] = None
    """
    The parameters for this activity
    """

    steps: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoActivityStep]],
        FieldMetadata(alias="Steps"),
        pydantic.Field(alias="Steps", description="The steps which are performed for this activity"),
    ] = None
    """
    The steps which are performed for this activity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
