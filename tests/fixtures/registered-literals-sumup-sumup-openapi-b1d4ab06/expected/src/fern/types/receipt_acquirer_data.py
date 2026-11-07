

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReceiptAcquirerData(UniversalBaseModel):
    """
    Acquirer-specific metadata related to the card authorization.
    """

    tid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of the terminal used for the authorization.
    """

    authorization_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization code returned by the acquirer.
    """

    return_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return code reported by the acquirer.
    """

    local_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local timestamp of the card authorization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
