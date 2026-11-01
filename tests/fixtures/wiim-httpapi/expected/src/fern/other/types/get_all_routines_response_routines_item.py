

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_all_routines_response_routines_item_steps_item import GetAllRoutinesResponseRoutinesItemStepsItem


class GetAllRoutinesResponseRoutinesItem(UniversalBaseModel):
    update_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updateDate"),
        pydantic.Field(alias="updateDate", description="Last update date of the routine"),
    ] = None
    """
    Last update date of the routine
    """

    steps: typing.Optional[typing.List[GetAllRoutinesResponseRoutinesItemStepsItem]] = pydantic.Field(default=None)
    """
    List of steps in the routine
    """

    create_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createDate"),
        pydantic.Field(alias="createDate", description="Creation date of the routine"),
    ] = None
    """
    Creation date of the routine
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the routine
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the routine
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Index of the routine
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
