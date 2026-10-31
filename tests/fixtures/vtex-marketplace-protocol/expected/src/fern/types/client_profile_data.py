

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClientProfileData(UniversalBaseModel):
    """
    Structure with the customer's information. An order will be identified as corporate if any of the corporate fields are filled out (`corporateDocument`, `corporatePhone`, `corporateName` or `tradeName`).
    """

    corporate_document: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporateDocument"),
        pydantic.Field(
            alias="corporateDocument",
            description="String with the company’s document number, in case of corporate orders.",
        ),
    ] = None
    """
    String with the company’s document number, in case of corporate orders.
    """

    corporate_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporateName"),
        pydantic.Field(
            alias="corporateName", description="String with the company’s name, in case of corporate orders."
        ),
    ] = None
    """
    String with the company’s name, in case of corporate orders.
    """

    corporate_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="corporatePhone"),
        pydantic.Field(
            alias="corporatePhone", description="String with the company’s phone number, in case of corporate orders."
        ),
    ] = None
    """
    String with the company’s phone number, in case of corporate orders.
    """

    document: str = pydantic.Field()
    """
    String with the customer’s document number.
    """

    email: str = pydantic.Field()
    """
    String with the customer's email.
    """

    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="String with the customer's first name."),
    ]
    """
    String with the customer's first name.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="String with the customer’s surname."),
    ]
    """
    String with the customer’s surname.
    """

    phone: str = pydantic.Field()
    """
    String with the customer’s phone number.
    """

    state_inscription: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stateInscription"),
        pydantic.Field(
            alias="stateInscription",
            description="String with the company’s state registration, in case of corporate orders.",
        ),
    ] = None
    """
    String with the company’s state registration, in case of corporate orders.
    """

    trade_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tradeName"),
        pydantic.Field(
            alias="tradeName", description="String with the company’s fantasy name, in case of corporate orders."
        ),
    ] = None
    """
    String with the company’s fantasy name, in case of corporate orders.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
