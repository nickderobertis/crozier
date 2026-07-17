

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Session(UniversalBaseModel):
    """
    Session
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Session ID.")
    ]
    """
    Session ID.
    """

    client_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientCode"),
        pydantic.Field(
            alias="clientCode",
            description="Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).",
        ),
    ]
    """
    Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    """

    client_engine: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientEngine"),
        pydantic.Field(alias="clientEngine", description="Client engine name."),
    ]
    """
    Client engine name.
    """

    client_engine_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientEngineVersion"),
        pydantic.Field(alias="clientEngineVersion", description="Client engine name."),
    ]
    """
    Client engine name.
    """

    client_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientName"), pydantic.Field(alias="clientName", description="Client name.")
    ]
    """
    Client name.
    """

    client_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientType"), pydantic.Field(alias="clientType", description="Client type.")
    ]
    """
    Client type.
    """

    client_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientVersion"), pydantic.Field(alias="clientVersion", description="Client version.")
    ]
    """
    Client version.
    """

    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="Country two-character ISO 3166-1 alpha code."),
    ]
    """
    Country two-character ISO 3166-1 alpha code.
    """

    country_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryName"), pydantic.Field(alias="countryName", description="Country name.")
    ]
    """
    Country name.
    """

    current: bool = pydantic.Field()
    """
    Returns true if this the current user session.
    """

    device_brand: typing_extensions.Annotated[
        str, FieldMetadata(alias="deviceBrand"), pydantic.Field(alias="deviceBrand", description="Device brand name.")
    ]
    """
    Device brand name.
    """

    device_model: typing_extensions.Annotated[
        str, FieldMetadata(alias="deviceModel"), pydantic.Field(alias="deviceModel", description="Device model name.")
    ]
    """
    Device model name.
    """

    device_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="deviceName"), pydantic.Field(alias="deviceName", description="Device name.")
    ]
    """
    Device name.
    """

    expire: int = pydantic.Field()
    """
    Session expiration date in Unix timestamp.
    """

    ip: str = pydantic.Field()
    """
    IP in use when the session was created.
    """

    os_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="osCode"),
        pydantic.Field(
            alias="osCode",
            description="Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).",
        ),
    ]
    """
    Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    """

    os_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="osName"), pydantic.Field(alias="osName", description="Operating system name.")
    ]
    """
    Operating system name.
    """

    os_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="osVersion"),
        pydantic.Field(alias="osVersion", description="Operating system version."),
    ]
    """
    Operating system version.
    """

    provider: str = pydantic.Field()
    """
    Session Provider.
    """

    provider_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="providerToken"),
        pydantic.Field(alias="providerToken", description="Session Provider Token."),
    ]
    """
    Session Provider Token.
    """

    provider_uid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="providerUid"),
        pydantic.Field(alias="providerUid", description="Session Provider User ID."),
    ]
    """
    Session Provider User ID.
    """

    user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId", description="User ID.")
    ]
    """
    User ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
