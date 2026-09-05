

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_secret_type import MutableSecretType
from .owner import Owner


class Secret(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="_id"), pydantic.Field(alias="_id")]
    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Secret creation time"),
    ]
    """
    Secret creation time
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Secret update time"),
    ] = None
    """
    Secret update time
    """

    value: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: str = pydantic.Field()
    """
    Human readable secret name
    """

    type: MutableSecretType
    owners: typing.List[Owner]
    tenant: typing.Optional[str] = None
    domain: typing.Optional[str] = None
    locked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lockedAt"),
        pydantic.Field(
            alias="lockedAt",
            description="Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.",
        ),
    ] = None
    """
    Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.
    """

    encrypted_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="encryptedFields"),
        pydantic.Field(alias="encryptedFields"),
    ] = None
    mixed_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="mixedProperties"),
        pydantic.Field(alias="mixedProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
