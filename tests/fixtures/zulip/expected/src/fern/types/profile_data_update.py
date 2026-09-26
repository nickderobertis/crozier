

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profile_data_update_value import ProfileDataUpdateValue


class ProfileDataUpdate(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    The ID of the custom profile field to update.
    """

    value: ProfileDataUpdateValue = pydantic.Field()
    """
    The new value for the user of the specified custom profile field.
    
    If null, then any value already set for the specified custom
    profile field will be removed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
