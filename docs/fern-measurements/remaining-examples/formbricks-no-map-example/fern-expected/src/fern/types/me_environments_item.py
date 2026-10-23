

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_environments_item_environment_type import MeEnvironmentsItemEnvironmentType
from .me_environments_item_permission import MeEnvironmentsItemPermission


class MeEnvironmentsItem(UniversalBaseModel):
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    environment_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="environmentId"), pydantic.Field(alias="environmentId")
    ]
    environment_type: typing_extensions.Annotated[
        MeEnvironmentsItemEnvironmentType,
        FieldMetadata(alias="environmentType"),
        pydantic.Field(alias="environmentType"),
    ]
    permission: MeEnvironmentsItemPermission
    project_id: typing_extensions.Annotated[str, FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")]
    project_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="projectName"), pydantic.Field(alias="projectName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
