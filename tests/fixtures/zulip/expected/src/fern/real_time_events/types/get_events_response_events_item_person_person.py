

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemPersonPerson(UniversalBaseModel):
    """
    Object containing details of the deactivated user.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the deactivated user.
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the user.
    
    **Deprecated**: We expect to remove this field in the future.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
