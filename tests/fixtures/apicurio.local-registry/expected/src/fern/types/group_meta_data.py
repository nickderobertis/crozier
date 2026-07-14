

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_id import GroupId
from .properties import Properties


class GroupMetaData(UniversalBaseModel):
    """ """

    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy")]
    created_on: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdOn")]
    description: str
    id: GroupId = pydantic.Field()
    """
    
    """

    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy")]
    modified_on: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="modifiedOn")]
    properties: Properties = pydantic.Field()
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
