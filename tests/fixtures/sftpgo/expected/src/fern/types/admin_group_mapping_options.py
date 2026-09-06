

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdminGroupMappingOptions(UniversalBaseModel):
    add_to_users_as: typing.Optional[str] = pydantic.Field(default=None)
    """
    Add to new users as:
      * `0` - the admin's group will be added as membership group for new users
      * `1` - the admin's group will be added as primary group for new users
      * `2` - the admin's group will be added as secondary group for new users
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
