

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_user import NestedUser
from .object_change_action import ObjectChangeAction


class ObjectChange(UniversalBaseModel):
    action: typing.Optional[ObjectChangeAction] = None
    changed_object: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    
    Serialize a nested representation of the changed object.
    """

    changed_object_id: int
    changed_object_type: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    postchange_data: typing.Optional[typing.Dict[str, typing.Any]] = None
    prechange_data: typing.Optional[typing.Dict[str, typing.Any]] = None
    request_id: typing.Optional[str] = None
    time: typing.Optional[dt.datetime] = None
    url: typing.Optional[str] = None
    user: typing.Optional[NestedUser] = None
    user_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
