

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presentation_network_auth import PresentationNetworkAuth
from .presentation_network_security import PresentationNetworkSecurity


class PresentationNetwork(UniversalBaseModel):
    id: str
    name: str
    ssid: str
    hidden: bool
    security: PresentationNetworkSecurity
    security_label: typing_extensions.Annotated[
        str, FieldMetadata(alias="securityLabel"), pydantic.Field(alias="securityLabel")
    ]
    auth: PresentationNetworkAuth
    credential_set: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="credentialSet"),
        pydantic.Field(
            alias="credentialSet", description="True means a credential exists; its value is never returned."
        ),
    ]
    """
    True means a credential exists; its value is never returned.
    """

    secret_updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="secretUpdatedAt"), pydantic.Field(alias="secretUpdatedAt")
    ] = None
    config_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="configRevision"), pydantic.Field(alias="configRevision")
    ]
    assigned_screens: typing_extensions.Annotated[
        int, FieldMetadata(alias="assignedScreens"), pydantic.Field(alias="assignedScreens")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
