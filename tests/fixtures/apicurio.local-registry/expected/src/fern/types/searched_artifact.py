

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_id import ArtifactId
from .artifact_state import ArtifactState
from .artifact_type import ArtifactType
from .group_id import GroupId


class SearchedArtifact(UniversalBaseModel):
    """
    Models a single artifact from the result set returned when searching for artifacts.
    """

    created_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy", description="")
    ]
    """
    
    """

    created_on: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn", description="")
    ]
    """
    
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    group_id: typing_extensions.Annotated[
        typing.Optional[GroupId], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId", description="")
    ] = None
    """
    
    """

    id: ArtifactId = pydantic.Field()
    """
    
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    
    """

    modified_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy", description="")
    ] = None
    """
    
    """

    modified_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifiedOn"),
        pydantic.Field(alias="modifiedOn", description=""),
    ] = None
    """
    
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    state: ArtifactState = pydantic.Field()
    """
    
    """

    type: ArtifactType = pydantic.Field()
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
