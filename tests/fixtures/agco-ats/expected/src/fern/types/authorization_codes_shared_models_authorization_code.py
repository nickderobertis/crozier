

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_codes_shared_models_parameter import AuthorizationCodesSharedModelsParameter


class AuthorizationCodesSharedModelsAuthorizationCode(UniversalBaseModel):
    """
    Represents the model containing an authorization code used to unlock a feature in machines and EDT
    """

    code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Code"),
        pydantic.Field(alias="Code", description="The code to enter to unlock a feature. Read only."),
    ] = None
    """
    The code to enter to unlock a feature. Read only.
    """

    created_by_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="CreatedByUserID"),
        pydantic.Field(
            alias="CreatedByUserID", description="The ID of the user that created this authorization code. Read only."
        ),
    ] = None
    """
    The ID of the user that created this authorization code. Read only.
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="A timestamp of when this code was created. Read only."),
    ] = None
    """
    A timestamp of when this code was created. Read only.
    """

    data_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsParameter]],
        FieldMetadata(alias="DataParameters"),
        pydantic.Field(
            alias="DataParameters",
            description="The parameters and values contained as data in this authorization code. May not be updated.",
        ),
    ] = None
    """
    The parameters and values contained as data in this authorization code. May not be updated.
    """

    definition_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefinitionID"),
        pydantic.Field(
            alias="DefinitionID",
            description="The id of the definition for this authorization code. May not be updated.",
        ),
    ] = None
    """
    The id of the definition for this authorization code. May not be updated.
    """

    deleted_by_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DeletedByUserID"),
        pydantic.Field(
            alias="DeletedByUserID", description="The ID of the user that deleted this authorization code. Read only."
        ),
    ] = None
    """
    The ID of the user that deleted this authorization code. Read only.
    """

    deleted_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DeletedDate"),
        pydantic.Field(
            alias="DeletedDate", description="A timestamp of when this authorization code was deleted. Read only."
        ),
    ] = None
    """
    A timestamp of when this authorization code was deleted. Read only.
    """

    effective_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EffectiveDate"),
        pydantic.Field(
            alias="EffectiveDate",
            description="A date at which this code should begin being valid. Optional. Set on create only.",
        ),
    ] = None
    """
    A date at which this code should begin being valid. Optional. Set on create only.
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The identifier for the authorization code. Read only."),
    ] = None
    """
    The identifier for the authorization code. Read only.
    """

    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsDeleted"),
        pydantic.Field(alias="IsDeleted", description="Indicates whether this code is deleted."),
    ] = None
    """
    Indicates whether this code is deleted.
    """

    validation_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsParameter]],
        FieldMetadata(alias="ValidationParameters"),
        pydantic.Field(
            alias="ValidationParameters",
            description="The parameters and values used to validate this authorization code. May not be updated.",
        ),
    ] = None
    """
    The parameters and values used to validate this authorization code. May not be updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
