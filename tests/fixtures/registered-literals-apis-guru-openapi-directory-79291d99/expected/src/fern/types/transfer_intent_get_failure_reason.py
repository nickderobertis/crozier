

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferIntentGetFailureReason(UniversalBaseModel):
    """
    The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise.
    """

    error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined).
    """

    error_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable description of the code associated with a failed transfer intent.
    """

    error_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A broad categorization of the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
