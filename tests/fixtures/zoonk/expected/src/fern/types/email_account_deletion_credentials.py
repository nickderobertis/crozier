

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmailAccountDeletionCredentials(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    Email address receiving the reauthentication code
    """

    otp: str = pydantic.Field()
    """
    Single-use email reauthentication code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
