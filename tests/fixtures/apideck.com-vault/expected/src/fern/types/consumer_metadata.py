

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConsumerMetadata(UniversalBaseModel):
    """
    The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended.
    """

    account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account as shown in the sidebar.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the user as shown in the sidebar.
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    The avatar of the user in the sidebar. Must be a valid URL
    """

    user_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the user as shown in the sidebar.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
