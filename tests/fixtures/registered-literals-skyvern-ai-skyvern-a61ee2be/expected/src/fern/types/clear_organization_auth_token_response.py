

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClearOrganizationAuthTokenResponse(UniversalBaseModel):
    """
    Response model for clearing an organization auth token.
    """

    success: bool = pydantic.Field()
    """
    Whether the token was cleared successfully
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
