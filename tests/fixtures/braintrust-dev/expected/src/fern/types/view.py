

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .acl_object_type import AclObjectType
from .view_data import ViewData
from .view_options import ViewOptions
from .view_view_type import ViewViewType


class View(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the view
    """

    object_type: AclObjectType
    object_id: str = pydantic.Field()
    """
    The id of the object the view applies to
    """

    view_type: ViewViewType = pydantic.Field()
    """
    Type of object that the view corresponds to.
    """

    name: str = pydantic.Field()
    """
    Name of the view
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of view creation
    """

    view_data: typing.Optional[ViewData] = None
    options: typing.Optional[ViewOptions] = None
    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the view
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of role deletion, or null if the role is still active
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
