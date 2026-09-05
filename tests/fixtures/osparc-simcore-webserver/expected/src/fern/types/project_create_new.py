

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_rights import AccessRights
from .study_ui_input import StudyUiInput


class ProjectCreateNew(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    name: str
    description: typing.Optional[str] = None
    thumbnail: typing.Optional[str] = None
    workbench: typing.Dict[str, typing.Any]
    access_rights: typing_extensions.Annotated[
        typing.Dict[str, AccessRights], FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ]
    tags: typing.Optional[typing.List[int]] = None
    classifiers: typing.Optional[typing.List[str]] = None
    ui: typing.Optional[StudyUiInput] = None
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
