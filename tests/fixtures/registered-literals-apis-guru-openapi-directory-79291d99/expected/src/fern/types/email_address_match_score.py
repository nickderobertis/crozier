

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmailAddressMatchScore(UniversalBaseModel):
    """
    Score found by matching email provided by the API with the email on the account at the financial institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled.
    """

    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Match score for normalized email. 100 is a perfect match and 0 is a no match. If the email is missing from either the API or financial institution, this is empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
