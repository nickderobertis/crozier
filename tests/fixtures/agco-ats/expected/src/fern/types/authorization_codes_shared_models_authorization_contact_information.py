

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorizationCodesSharedModelsAuthorizationContactInformation(UniversalBaseModel):
    authorization_code_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="AuthorizationCodeID"),
        pydantic.Field(
            alias="AuthorizationCodeID", description="AuthorizationCode ID that the contact information ties into."
        ),
    ]
    """
    AuthorizationCode ID that the contact information ties into.
    """

    code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Code"),
        pydantic.Field(alias="Code", description="The authorization code. Read Only."),
    ] = None
    """
    The authorization code. Read Only.
    """

    contact: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Contact"),
        pydantic.Field(
            alias="Contact",
            description="Name of contact requesting an authorization code. Minimum length of 3 characters.",
        ),
    ]
    """
    Name of contact requesting an authorization code. Minimum length of 3 characters.
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CreatedBy"),
        pydantic.Field(alias="CreatedBy", description="The name of the user that created this code. Read Only."),
    ] = None
    """
    The name of the user that created this code. Read Only.
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="The date the authorization code was created."),
    ] = None
    """
    The date the authorization code was created.
    """

    dealer_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DealerCode"),
        pydantic.Field(
            alias="DealerCode",
            description="Dealer code that relates to the dealership. Minimum length of 3 characters.",
        ),
    ]
    """
    Dealer code that relates to the dealership. Minimum length of 3 characters.
    """

    dealership: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Dealership"),
        pydantic.Field(alias="Dealership", description="Name of dealership. Minimum length of 3 characters."),
    ]
    """
    Name of dealership. Minimum length of 3 characters.
    """

    definition_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefinitionName"),
        pydantic.Field(
            alias="DefinitionName",
            description="The name of the definition used for generating this authorization code. Read Only.",
        ),
    ] = None
    """
    The name of the definition used for generating this authorization code. Read Only.
    """

    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="Email of contact."),
    ] = None
    """
    Email of contact.
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="ID of authorizationContactInformation"),
    ] = None
    """
    ID of authorizationContactInformation
    """

    notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Optional notes used for internal use."),
    ] = None
    """
    Optional notes used for internal use.
    """

    phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="Phone"), pydantic.Field(alias="Phone", description="Phone number of contact.")
    ]
    """
    Phone number of contact.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
