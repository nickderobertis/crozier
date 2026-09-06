

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .acl_object_type import AclObjectType
from .create_view_view_type import CreateViewViewType
from .view_data import ViewData
from .view_options import ViewOptions


class CreateView(UniversalBaseModel):
    object_type: AclObjectType
    object_id: str = pydantic.Field()
    """
    The id of the object the view applies to
    """

    view_type: CreateViewViewType = pydantic.Field()
    """
    Type of object that the view corresponds to.
    """

    name: str = pydantic.Field()
    """
    Name of the view
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
