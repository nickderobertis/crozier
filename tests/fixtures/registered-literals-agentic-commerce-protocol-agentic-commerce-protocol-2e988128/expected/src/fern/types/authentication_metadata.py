

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_acquirer_details import AuthenticationMetadataAcquirerDetails
from .authentication_metadata_channel import AuthenticationMetadataChannel
from .authentication_metadata_directory_server import AuthenticationMetadataDirectoryServer
from .authentication_metadata_flow_preference import AuthenticationMetadataFlowPreference


class AuthenticationMetadata(UniversalBaseModel):
    """
    Seller-provided authentication metadata for 3DS flows.
    """

    channel: AuthenticationMetadataChannel = pydantic.Field()
    """
    Details about the channel used for this 3DS Authentication.
    """

    acquirer_details: AuthenticationMetadataAcquirerDetails = pydantic.Field()
    """
    Details about the acquirer used for this 3DS Authentication. This object MUST be present.
    """

    directory_server: AuthenticationMetadataDirectoryServer = pydantic.Field()
    """
    The 3DS directory server used for this Authentication.
    """

    flow_preference: typing.Optional[AuthenticationMetadataFlowPreference] = pydantic.Field(default=None)
    """
    Contains additional details on the seller's preference for the 3DS authentication flow. Sellers MAY request a preference, but issuers ultimately decide the actual flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
