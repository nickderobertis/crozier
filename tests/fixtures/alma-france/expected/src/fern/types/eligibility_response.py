

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EligibilityResponse(UniversalBaseModel):
    eligible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the purchase is eligible
    """

    reasons: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Reasons if not eligible
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
