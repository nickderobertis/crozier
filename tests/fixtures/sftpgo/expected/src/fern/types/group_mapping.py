

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroupMapping(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    group name
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Group type:
      * `1` - Primary group
      * `2` - Secondary group
      * `3` - Membership only, no settings are inherited from this group type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
