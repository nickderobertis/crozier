

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bunq_id import BunqId
from .installation_server_public_key import InstallationServerPublicKey
from .installation_token import InstallationToken


class InstallationCreate(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[BunqId],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The Id object of the created Installation"),
    ] = None
    """
    The Id object of the created Installation
    """

    server_public_key: typing_extensions.Annotated[
        typing.Optional[InstallationServerPublicKey],
        FieldMetadata(alias="ServerPublicKey"),
        pydantic.Field(alias="ServerPublicKey", description="The ServerPublicKey object of the created Installation"),
    ] = None
    """
    The ServerPublicKey object of the created Installation
    """

    token: typing_extensions.Annotated[
        typing.Optional[InstallationToken],
        FieldMetadata(alias="Token"),
        pydantic.Field(alias="Token", description="The Token object of this Installation."),
    ] = None
    """
    The Token object of this Installation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
