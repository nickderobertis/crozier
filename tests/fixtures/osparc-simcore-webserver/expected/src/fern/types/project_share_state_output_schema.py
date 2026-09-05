

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_id_int import GroupIdInt
from .project_status import ProjectStatus


class ProjectShareStateOutputSchema(UniversalBaseModel):
    status: ProjectStatus = pydantic.Field()
    """
    The status of the project
    """

    locked: bool = pydantic.Field()
    """
    True if the project is locked
    """

    current_user_groupids: typing_extensions.Annotated[
        typing.List[GroupIdInt],
        FieldMetadata(alias="currentUserGroupids"),
        pydantic.Field(
            alias="currentUserGroupids",
            description="Current users in the project (if the project is locked, the list contains only the lock owner)",
        ),
    ]
    """
    Current users in the project (if the project is locked, the list contains only the lock owner)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
