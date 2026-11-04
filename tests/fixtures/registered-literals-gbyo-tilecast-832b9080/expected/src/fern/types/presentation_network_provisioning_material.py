

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presentation_network_auth import PresentationNetworkAuth
from .presentation_network_security import PresentationNetworkSecurity


class PresentationNetworkProvisioningMaterial(UniversalBaseModel):
    presentation_network_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="presentationNetworkId"), pydantic.Field(alias="presentationNetworkId")
    ]
    name: str
    ssid: str
    hidden: bool
    security: PresentationNetworkSecurity
    auth: PresentationNetworkAuth
    config_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="configRevision"), pydantic.Field(alias="configRevision")
    ]
    profile_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="profileName"), pydantic.Field(alias="profileName")
    ]
    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plaintext credential returned only to the authenticated player over a no-store response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
