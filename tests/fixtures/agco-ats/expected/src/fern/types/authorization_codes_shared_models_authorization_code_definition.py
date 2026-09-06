

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_codes_shared_models_authorization_code_definition_duration_units import (
    AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits,
)
from .authorization_codes_shared_models_data_field import AuthorizationCodesSharedModelsDataField
from .authorization_codes_shared_models_validation_field import AuthorizationCodesSharedModelsValidationField


class AuthorizationCodesSharedModelsAuthorizationCodeDefinition(UniversalBaseModel):
    """
    Represents the model used to define how a type of authorization code is generated.
    """

    authorization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorizationID"),
        pydantic.Field(alias="AuthorizationID", description="The value used for securing codes generated."),
    ] = None
    """
    The value used for securing codes generated.
    """

    created_by_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="CreatedByUserID"),
        pydantic.Field(
            alias="CreatedByUserID", description="The ID of the user that created this definition. Read only."
        ),
    ] = None
    """
    The ID of the user that created this definition. Read only.
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="A timestamp of when this definition was created. Read only."),
    ] = None
    """
    A timestamp of when this definition was created. Read only.
    """

    data_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsDataField]],
        FieldMetadata(alias="DataFields"),
        pydantic.Field(
            alias="DataFields",
            description="The defined fields to include in authorization codes generated from this definition. May not be updated.",
        ),
    ] = None
    """
    The defined fields to include in authorization codes generated from this definition. May not be updated.
    """

    deleted_by_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DeletedByUserID"),
        pydantic.Field(
            alias="DeletedByUserID", description="The ID of the user that deleted this definition. Read only."
        ),
    ] = None
    """
    The ID of the user that deleted this definition. Read only.
    """

    deleted_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DeletedDate"),
        pydantic.Field(alias="DeletedDate", description="A timestamp of when this definition was deleted. Read only."),
    ] = None
    """
    A timestamp of when this definition was deleted. Read only.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="A description of this definition. May not be updated."),
    ] = None
    """
    A description of this definition. May not be updated.
    """

    duration_accuracy: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DurationAccuracy"),
        pydantic.Field(
            alias="DurationAccuracy",
            description="The number of bits used for timestamp verification. Defaults to 5. May not be updated.",
        ),
    ] = None
    """
    The number of bits used for timestamp verification. Defaults to 5. May not be updated.
    """

    duration_amount: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DurationAmount"),
        pydantic.Field(
            alias="DurationAmount",
            description="The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.",
        ),
    ] = None
    """
    The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.
    """

    duration_units: typing_extensions.Annotated[
        typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits],
        FieldMetadata(alias="DurationUnits"),
        pydantic.Field(
            alias="DurationUnits",
            description="The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.",
        ),
    ] = None
    """
    The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.
    """

    hash_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="HashLength"),
        pydantic.Field(
            alias="HashLength",
            description="The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.",
        ),
    ] = None
    """
    The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The ID of the authorization code definition. Read only."),
    ] = None
    """
    The ID of the authorization code definition. Read only.
    """

    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsDeleted"),
        pydantic.Field(
            alias="IsDeleted",
            description="Indicates whether this definition is enabled. True if generating codes is disabled.",
        ),
    ] = None
    """
    Indicates whether this definition is enabled. True if generating codes is disabled.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the authorization code definition. May not be updated."),
    ]
    """
    The name of the authorization code definition. May not be updated.
    """

    random_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="RandomLength"),
        pydantic.Field(
            alias="RandomLength",
            description='The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.',
        ),
    ] = None
    """
    The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.
    """

    validation_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsValidationField]],
        FieldMetadata(alias="ValidationFields"),
        pydantic.Field(
            alias="ValidationFields",
            description="The defined fields to verify when reading authorization codes generated from this definition. May not be updated.",
        ),
    ] = None
    """
    The defined fields to verify when reading authorization codes generated from this definition. May not be updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
