

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Meta(UniversalBaseModel):
    """
    Allows specifying the metadata of the test account
    """

    limit: float = pydantic.Field()
    """
    The account's limit
    """

    mask: str = pydantic.Field()
    """
    The account's mask. Should be a string of 2-4 alphanumeric characters. This allows you to model a mask which does not match the account number (such as with a virtual account number).
    """

    name: str = pydantic.Field()
    """
    The account's name
    """

    official_name: str = pydantic.Field()
    """
    The account's official name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
