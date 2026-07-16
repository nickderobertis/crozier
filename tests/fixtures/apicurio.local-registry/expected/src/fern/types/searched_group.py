

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_id import GroupId


class SearchedGroup(UniversalBaseModel):
    """
    Models a single group from the result set returned when searching for groups.
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

    description: str = pydantic.Field()
    """
    
    """

    id: GroupId = pydantic.Field()
    """
    
    """

    modified_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy", description="")
    ]
    """
    
    """

    modified_on: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedOn"), pydantic.Field(alias="modifiedOn", description="")
    ]
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
