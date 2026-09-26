

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PrivilegesDataItem(UniversalBaseModel):
    object_type: str = pydantic.Field()
    """
      The type of the object to which the privilege belongs.
    """

    privilege: str = pydantic.Field()
    """
      The privilege that is granted to the role.
    """

    object_name: str = pydantic.Field()
    """
      The name of the object to which the role is granted the specified privilege.
    """

    db_name: str = pydantic.Field()
    """
      The name of the database in which this operation has been executed.
    """

    grantor: typing.Optional[str] = pydantic.Field(default=None)
    """
      The name of the user who granted a specific role to a user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
