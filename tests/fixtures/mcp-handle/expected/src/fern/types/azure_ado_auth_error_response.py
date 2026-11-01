

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AzureAdoAuthErrorResponse(UniversalBaseModel):
    error: str = pydantic.Field()
    """
    Error message from the OAuth process
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
