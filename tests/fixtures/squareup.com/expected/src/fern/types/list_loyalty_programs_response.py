

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .loyalty_program import LoyaltyProgram


class ListLoyaltyProgramsResponse(UniversalBaseModel):
    """
    A response that contains all loyalty programs.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    programs: typing.Optional[typing.List[LoyaltyProgram]] = pydantic.Field(default=None)
    """
    A list of `LoyaltyProgram` for the merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
