

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .super_fund_type import SuperFundType
from .validation_error import ValidationError


class SuperFund(UniversalBaseModel):
    abn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ABN"),
        pydantic.Field(alias="ABN", description="ABN of the self managed super fund"),
    ] = None
    """
    ABN of the self managed super fund
    """

    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountName"),
        pydantic.Field(alias="AccountName", description="The account name for the self managed super fund."),
    ] = None
    """
    The account name for the self managed super fund.
    """

    account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountNumber"),
        pydantic.Field(alias="AccountNumber", description="The account number for the self managed super fund."),
    ] = None
    """
    The account number for the self managed super fund.
    """

    bsb: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BSB"),
        pydantic.Field(alias="BSB", description="BSB of the self managed super fund"),
    ] = None
    """
    BSB of the self managed super fund
    """

    electronic_service_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ElectronicServiceAddress"),
        pydantic.Field(
            alias="ElectronicServiceAddress",
            description="The electronic service address for the self managed super fund.",
        ),
    ] = None
    """
    The electronic service address for the self managed super fund.
    """

    employer_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployerNumber"),
        pydantic.Field(alias="EmployerNumber", description="Some funds assign a unique number to each employer"),
    ] = None
    """
    Some funds assign a unique number to each employer
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Name of the super fund"),
    ] = None
    """
    Name of the super fund
    """

    spin: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SPIN"),
        pydantic.Field(
            alias="SPIN",
            description="The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN.",
        ),
    ] = None
    """
    The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN.
    """

    super_fund_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SuperFundID"),
        pydantic.Field(alias="SuperFundID", description="Xero identifier for a super fund"),
    ] = None
    """
    Xero identifier for a super fund
    """

    type: typing_extensions.Annotated[SuperFundType, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")]
    usi: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="USI"),
        pydantic.Field(alias="USI", description="The USI of the Regulated SuperFund"),
    ] = None
    """
    The USI of the Regulated SuperFund
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationError]],
        FieldMetadata(alias="ValidationErrors"),
        pydantic.Field(
            alias="ValidationErrors", description="Displays array of validation error messages from the API"
        ),
    ] = None
    """
    Displays array of validation error messages from the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
