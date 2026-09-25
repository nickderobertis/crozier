

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagesEventDisplayRecipientOneItem(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Zulip API email of the user.
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the user.
    """

    is_mirror_dummy: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is a mirror dummy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
