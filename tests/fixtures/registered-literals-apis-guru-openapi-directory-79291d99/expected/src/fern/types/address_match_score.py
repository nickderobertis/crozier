

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AddressMatchScore(UniversalBaseModel):
    """
    Score found by matching address provided by the API with the address on the account at the financial institution. The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled.
    """

    is_postal_code_match: typing.Optional[bool] = pydantic.Field(default=None)
    """
    postal code was provided for both and was a match
    """

    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Match score for address. The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the address is missing from either the API or financial institution, this is empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
