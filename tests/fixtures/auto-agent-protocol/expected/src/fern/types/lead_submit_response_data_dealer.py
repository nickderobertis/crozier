

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LeadSubmitResponseDataDealer(UniversalBaseModel):
    """
    Convenience contact summary for the buyer agent to surface follow-up details to the user.
    """

    name: typing.Optional[str] = None
    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    E.164 phone number for buyer follow-up.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
