

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class RelationUser(UniversalBaseModel):
    counter_label_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The counter user's label.
    """

    counter_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The counter user's ID.
    """

    counter_user_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account status of a user
    """

    label_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user's label.
    """

    relationship: typing.Optional[str] = pydantic.Field(default=None)
    """
    The requested relation type.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request's status, only for UPDATE.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's ID.
    """

    user_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account status of a user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
