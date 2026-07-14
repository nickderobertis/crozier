

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Session(UniversalBaseModel):
    """
    Session
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    Session ID.
    """

    client_code: typing_extensions.Annotated[str, FieldMetadata(alias="clientCode")] = pydantic.Field()
    """
    Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    """

    client_engine: typing_extensions.Annotated[str, FieldMetadata(alias="clientEngine")] = pydantic.Field()
    """
    Client engine name.
    """

    client_engine_version: typing_extensions.Annotated[str, FieldMetadata(alias="clientEngineVersion")] = (
        pydantic.Field()
    )
    """
    Client engine name.
    """

    client_name: typing_extensions.Annotated[str, FieldMetadata(alias="clientName")] = pydantic.Field()
    """
    Client name.
    """

    client_type: typing_extensions.Annotated[str, FieldMetadata(alias="clientType")] = pydantic.Field()
    """
    Client type.
    """

    client_version: typing_extensions.Annotated[str, FieldMetadata(alias="clientVersion")] = pydantic.Field()
    """
    Client version.
    """

    country_code: typing_extensions.Annotated[str, FieldMetadata(alias="countryCode")] = pydantic.Field()
    """
    Country two-character ISO 3166-1 alpha code.
    """

    country_name: typing_extensions.Annotated[str, FieldMetadata(alias="countryName")] = pydantic.Field()
    """
    Country name.
    """

    current: bool = pydantic.Field()
    """
    Returns true if this the current user session.
    """

    device_brand: typing_extensions.Annotated[str, FieldMetadata(alias="deviceBrand")] = pydantic.Field()
    """
    Device brand name.
    """

    device_model: typing_extensions.Annotated[str, FieldMetadata(alias="deviceModel")] = pydantic.Field()
    """
    Device model name.
    """

    device_name: typing_extensions.Annotated[str, FieldMetadata(alias="deviceName")] = pydantic.Field()
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

    os_code: typing_extensions.Annotated[str, FieldMetadata(alias="osCode")] = pydantic.Field()
    """
    Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    """

    os_name: typing_extensions.Annotated[str, FieldMetadata(alias="osName")] = pydantic.Field()
    """
    Operating system name.
    """

    os_version: typing_extensions.Annotated[str, FieldMetadata(alias="osVersion")] = pydantic.Field()
    """
    Operating system version.
    """

    provider: str = pydantic.Field()
    """
    Session Provider.
    """

    provider_token: typing_extensions.Annotated[str, FieldMetadata(alias="providerToken")] = pydantic.Field()
    """
    Session Provider Token.
    """

    provider_uid: typing_extensions.Annotated[str, FieldMetadata(alias="providerUid")] = pydantic.Field()
    """
    Session Provider User ID.
    """

    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId")] = pydantic.Field()
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
