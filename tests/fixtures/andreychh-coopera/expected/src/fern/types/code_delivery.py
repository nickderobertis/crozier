

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeDelivery(UniversalBaseModel):
    """
    Says that a code was sent. It carries neither the code nor the address on purpose: the code belongs in the mailbox, and the address is what the caller has just supplied.
    """

    expires_in: int = pydantic.Field()
    """
    Seconds the code just sent will keep working.
    """

    retry_after: int = pydantic.Field()
    """
    Seconds before another code may be requested for this address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
