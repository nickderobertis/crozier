

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_collection_item_roles_item import UserCollectionItemRolesItem


class UserCollectionItem(UniversalBaseModel):
    """
    A user object.

    *New in version 2.1.0*
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is active
    """

    changed_on: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date user was changed
    """

    created_on: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date user was created
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email.
    
    *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.
    """

    failed_login_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of times the login failed
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's first name.
    
    *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.
    """

    last_login: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last user login
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's last name.
    
    *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.
    """

    login_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The login count
    """

    roles: typing.Optional[typing.List[typing.Optional[UserCollectionItemRolesItem]]] = pydantic.Field(default=None)
    """
    User roles.
    
    *Changed in version 2.2.0*&#58; Field is no longer read-only.
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username.
    
    *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
