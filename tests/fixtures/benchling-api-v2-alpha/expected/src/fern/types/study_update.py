

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fields import Fields
from .study_update_phase import StudyUpdatePhase


class StudyUpdate(UniversalBaseModel):
    archive_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="archiveReason"), pydantic.Field(alias="archiveReason")
    ] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the Study.
    """

    fields: typing.Optional[Fields] = None
    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that contains the Study."),
    ] = None
    """
    ID of the folder that contains the Study.
    """

    id: typing.Optional[str] = None
    is_archived: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isArchived"), pydantic.Field(alias="isArchived")
    ] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Study.
    """

    phase: typing.Optional[StudyUpdatePhase] = pydantic.Field(default=None)
    """
    The phase of the Study.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
