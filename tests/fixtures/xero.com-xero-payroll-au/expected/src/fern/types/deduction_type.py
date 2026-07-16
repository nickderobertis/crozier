

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deduction_type_deduction_category import DeductionTypeDeductionCategory


class DeductionType(UniversalBaseModel):
    account_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountCode"),
        pydantic.Field(alias="AccountCode", description="See Accounts"),
    ] = None
    """
    See Accounts
    """

    current_record: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="CurrentRecord"),
        pydantic.Field(alias="CurrentRecord", description="Is the current record"),
    ] = None
    """
    Is the current record
    """

    deduction_category: typing_extensions.Annotated[
        typing.Optional[DeductionTypeDeductionCategory],
        FieldMetadata(alias="DeductionCategory"),
        pydantic.Field(alias="DeductionCategory"),
    ] = None
    deduction_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DeductionTypeID"),
        pydantic.Field(alias="DeductionTypeID", description="Xero identifier"),
    ] = None
    """
    Xero identifier
    """

    is_exempt_from_w1: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsExemptFromW1"),
        pydantic.Field(
            alias="IsExemptFromW1",
            description="Boolean to determine if the deduction type is reportable or exempt from W1",
        ),
    ] = None
    """
    Boolean to determine if the deduction type is reportable or exempt from W1
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Name of the earnings rate (max length = 100)"),
    ] = None
    """
    Name of the earnings rate (max length = 100)
    """

    reduces_super: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ReducesSuper"),
        pydantic.Field(
            alias="ReducesSuper",
            description="Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this.",
        ),
    ] = None
    """
    Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this.
    """

    reduces_tax: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ReducesTax"),
        pydantic.Field(
            alias="ReducesTax",
            description="Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee.",
        ),
    ] = None
    """
    Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee.
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
