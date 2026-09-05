

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_rights import AccessRights
from .group_id_int import GroupIdInt
from .lower_case_email_str import LowerCaseEmailStr
from .project_get_thumbnail import ProjectGetThumbnail
from .project_get_ui import ProjectGetUi
from .project_permalink import ProjectPermalink
from .project_state_output_schema import ProjectStateOutputSchema
from .project_template_type import ProjectTemplateType
from .project_type import ProjectType


class ProjectGet(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    name: str
    description: str
    thumbnail: ProjectGetThumbnail
    type: ProjectType
    template_type: typing_extensions.Annotated[
        typing.Optional[ProjectTemplateType], FieldMetadata(alias="templateType"), pydantic.Field(alias="templateType")
    ] = None
    workbench: typing.Dict[str, typing.Any]
    prj_owner: typing_extensions.Annotated[
        LowerCaseEmailStr, FieldMetadata(alias="prjOwner"), pydantic.Field(alias="prjOwner")
    ]
    access_rights: typing_extensions.Annotated[
        typing.Dict[str, AccessRights], FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ]
    creation_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="creationDate"), pydantic.Field(alias="creationDate")
    ]
    last_change_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastChangeDate"), pydantic.Field(alias="lastChangeDate")
    ]
    state: typing.Optional[ProjectStateOutputSchema] = None
    trashed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="trashedAt"), pydantic.Field(alias="trashedAt")
    ] = None
    trashed_by: typing_extensions.Annotated[
        typing.Optional[GroupIdInt],
        FieldMetadata(alias="trashedBy"),
        pydantic.Field(alias="trashedBy", description="The primary gid of the user who trashed"),
    ] = None
    """
    The primary gid of the user who trashed
    """

    tags: typing.List[int]
    classifiers: typing.Optional[typing.List[str]] = None
    quality: typing.Optional[typing.Dict[str, typing.Any]] = None
    ui: typing.Optional[ProjectGetUi] = None
    dev: typing.Optional[typing.Dict[str, typing.Any]] = None
    permalink: typing.Optional[ProjectPermalink] = None
    workspace_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ] = None
    folder_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
