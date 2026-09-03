

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClaimStatus(UniversalBaseModel):
    """
    Resolved claims among the RP requested claims with their availability and verification status.
    """

    claim: str = pydantic.Field()
    """
    Claim name.
    """

    available: bool = pydantic.Field()
    """
    True if the claim is available for the user account.
    """

    verified: bool = pydantic.Field()
    """
    True only if the claim is available and verified by atleast one trust framework. And also the verification process completed before the requested max_age.
    """

    purpose: typing.Optional[str] = pydantic.Field(default=None)
    """
    Purpose of the claim as provided in the authorize request by the relying party
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
