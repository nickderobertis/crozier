

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NameMatchScore(UniversalBaseModel):
    """
    Score found by matching name provided by the API with the name on the account at the financial institution. If the account contains multiple owners, the maximum match score is filled.
    """

    is_business_name_detected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is `true` if the name on either of the names that was matched for the score contained strings indicative of a business name, such as "CORP", "LLC", "INC", or "LTD". A `true` result generally indicates the entity is a business. However, a `false` result does not mean the entity is not a business, as some businesses do not use these strings in the names used for their financial institution accounts.
    """

    is_first_name_or_last_name_match: typing.Optional[bool] = pydantic.Field(default=None)
    """
    first or last name completely matched, likely a family member
    """

    is_nickname_match: typing.Optional[bool] = pydantic.Field(default=None)
    """
    nickname matched, example Jennifer and Jenn.
    """

    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Represents the match score for name. 100 is a perfect score, 85-99 means a strong match, 50-84 is a partial match, less than 50 is a weak match and 0 is a complete mismatch. If the name is missing from either the API or financial institution, this is empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
