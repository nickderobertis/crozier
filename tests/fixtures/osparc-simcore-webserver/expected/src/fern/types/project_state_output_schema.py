

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_running_state import ProjectRunningState
from .project_share_state_output_schema import ProjectShareStateOutputSchema


class ProjectStateOutputSchema(UniversalBaseModel):
    share_state: typing_extensions.Annotated[
        ProjectShareStateOutputSchema, FieldMetadata(alias="shareState"), pydantic.Field(alias="shareState")
    ]
    state: ProjectRunningState = pydantic.Field()
    """
    The project running state
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
