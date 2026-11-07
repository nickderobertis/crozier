

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthenticationMetadataAcquirerDetails(UniversalBaseModel):
    """
    Details about the acquirer used for this 3DS Authentication. This object MUST be present.
    """

    acquirer_bin: str = pydantic.Field()
    """
    The Acquirer BIN (directory-server specific).
    """

    acquirer_country: str = pydantic.Field()
    """
    Two-letter ISO 3166-1 alpha-2 country code.
    """

    acquirer_merchant_id: str = pydantic.Field()
    """
    The Merchant ID assigned by the acquirer.
    """

    merchant_name: str = pydantic.Field()
    """
    Merchant name assigned by the acquirer.
    """

    requestor_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Requestor ID (if required by the directory server).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
