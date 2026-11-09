

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_acquirer_details import AuthenticationMetadataAcquirerDetails
from .authentication_metadata_channel import AuthenticationMetadataChannel
from .authentication_metadata_directory_server import AuthenticationMetadataDirectoryServer
from .authentication_metadata_flow_preference import AuthenticationMetadataFlowPreference


class AuthenticationMetadata(UniversalBaseModel):
    channel: AuthenticationMetadataChannel
    acquirer_details: AuthenticationMetadataAcquirerDetails
    directory_server: AuthenticationMetadataDirectoryServer
    flow_preference: typing.Optional[AuthenticationMetadataFlowPreference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
