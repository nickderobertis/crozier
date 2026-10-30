

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class OrderPlacementClientProfileData(UniversalBaseModel):
    """
    Customer's profile information.
    """

    corporate_document: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporateDocument"),
        pydantic.Field(alias="corporateDocument", description="Corporate document, if the customer is a legal entity."),
    ] = None
    """
    Corporate document, if the customer is a legal entity.
    """

    corporate_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporateName"),
        pydantic.Field(alias="corporateName", description="Company name, if the customer is a legal entity."),
    ] = None
    """
    Company name, if the customer is a legal entity.
    """

    corporate_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporatePhone"),
        pydantic.Field(
            alias="corporatePhone", description="Corporate phone number, if the customer is a legal entity."
        ),
    ] = None
    """
    Corporate phone number, if the customer is a legal entity.
    """

    document: str = pydantic.Field()
    """
    Document number informed by the customer.
    """

    document_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Type of the document informed by the customer."),
    ]
    """
    Type of the document informed by the customer.
    """

    email: str = pydantic.Field()
    """
    Customer's email address.
    """

    first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName", description="Customer's first name.")
    ]
    """
    Customer's first name.
    """

    is_corporate: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCorporate"),
        pydantic.Field(alias="isCorporate", description="`true` if the customer is a legal entity."),
    ] = None
    """
    `true` if the customer is a legal entity.
    """

    last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName", description="Customer's last name.")
    ]
    """
    Customer's last name.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer's phone number.
    """

    state_inscription: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stateInscription"),
        pydantic.Field(alias="stateInscription", description="State inscription, if the customer is a legal entity."),
    ] = None
    """
    State inscription, if the customer is a legal entity.
    """

    trade_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tradeName"),
        pydantic.Field(alias="tradeName", description="Trade name, if the customer is a legal entity."),
    ] = None
    """
    Trade name, if the customer is a legal entity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
