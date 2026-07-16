

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_id import ArtifactId
from .artifact_reference import ArtifactReference
from .artifact_state import ArtifactState
from .artifact_type import ArtifactType
from .group_id import GroupId
from .properties import Properties


class ArtifactMetaData(UniversalBaseModel):
    """ """

    content_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId", description="")
    ]
    """
    
    """

    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    created_on: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn")
    ]
    description: typing.Optional[str] = None
    global_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="globalId"), pydantic.Field(alias="globalId", description="")
    ]
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

    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modified_on: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedOn"), pydantic.Field(alias="modifiedOn")
    ]
    name: typing.Optional[str] = None
    properties: typing.Optional[Properties] = pydantic.Field(default=None)
    """
    
    """

    references: typing.Optional[typing.List[ArtifactReference]] = pydantic.Field(default=None)
    """
    
    """

    state: ArtifactState = pydantic.Field()
    """
    
    """

    type: ArtifactType = pydantic.Field()
    """
    
    """

    version: str = pydantic.Field()
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
