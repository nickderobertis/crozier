

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_reference import ArtifactReference
from .artifact_state import ArtifactState
from .artifact_type import ArtifactType
from .properties import Properties


class SearchedVersion(UniversalBaseModel):
    """
    Models a single artifact from the result set returned when searching for artifacts.
    """

    content_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId", description="")
    ]
    """
    
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

    global_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="globalId"), pydantic.Field(alias="globalId", description="")
    ]
    """
    
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    properties: typing.Optional[Properties] = pydantic.Field(default=None)
    """
    
    """

    references: typing.List[ArtifactReference] = pydantic.Field()
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
