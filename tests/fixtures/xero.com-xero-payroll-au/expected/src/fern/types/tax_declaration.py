

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .employment_basis import EmploymentBasis
from .residency_status import ResidencyStatus
from .tfn_exemption_type import TfnExemptionType


class TaxDeclaration(UniversalBaseModel):
    approved_withholding_variation_percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ApprovedWithholdingVariationPercentage"),
        pydantic.Field(
            alias="ApprovedWithholdingVariationPercentage",
            description="If the employee has approved withholding variation. e.g (0 - 100)",
        ),
    ] = None
    """
    If the employee has approved withholding variation. e.g (0 - 100)
    """

    australian_resident_for_tax_purposes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AustralianResidentForTaxPurposes"),
        pydantic.Field(
            alias="AustralianResidentForTaxPurposes",
            description="If the employee is Australian resident for tax purposes. e.g true or false",
        ),
    ] = None
    """
    If the employee is Australian resident for tax purposes. e.g true or false
    """

    eligible_to_receive_leave_loading: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="EligibleToReceiveLeaveLoading"),
        pydantic.Field(
            alias="EligibleToReceiveLeaveLoading",
            description="If the employee is eligible to receive an additional percentage on top of ordinary earnings when they take leave (typically 17.5%). e.g true or false",
        ),
    ] = None
    """
    If the employee is eligible to receive an additional percentage on top of ordinary earnings when they take leave (typically 17.5%). e.g true or false
    """

    employee_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployeeID"),
        pydantic.Field(alias="EmployeeID", description="Address line 1 for employee home address"),
    ] = None
    """
    Address line 1 for employee home address
    """

    employment_basis: typing_extensions.Annotated[
        typing.Optional[EmploymentBasis],
        FieldMetadata(alias="EmploymentBasis"),
        pydantic.Field(alias="EmploymentBasis"),
    ] = None
    has_help_debt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="HasHELPDebt"),
        pydantic.Field(alias="HasHELPDebt", description="If employee has HECS or HELP debt. e.g true or false"),
    ] = None
    """
    If employee has HECS or HELP debt. e.g true or false
    """

    has_sfss_debt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="HasSFSSDebt"),
        pydantic.Field(alias="HasSFSSDebt", description="If employee has financial supplement debt. e.g true or false"),
    ] = None
    """
    If employee has financial supplement debt. e.g true or false
    """

    has_student_startup_loan: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="HasStudentStartupLoan"),
        pydantic.Field(
            alias="HasStudentStartupLoan", description="If the employee is eligible for student startup loan rules"
        ),
    ] = None
    """
    If the employee is eligible for student startup loan rules
    """

    has_trade_support_loan_debt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="HasTradeSupportLoanDebt"),
        pydantic.Field(
            alias="HasTradeSupportLoanDebt", description="If employee has trade support loan. e.g true or false"
        ),
    ] = None
    """
    If employee has trade support loan. e.g true or false
    """

    residency_status: typing_extensions.Annotated[
        typing.Optional[ResidencyStatus],
        FieldMetadata(alias="ResidencyStatus"),
        pydantic.Field(alias="ResidencyStatus"),
    ] = None
    tfn_exemption_type: typing_extensions.Annotated[
        typing.Optional[TfnExemptionType],
        FieldMetadata(alias="TFNExemptionType"),
        pydantic.Field(alias="TFNExemptionType"),
    ] = None
    tax_file_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TaxFileNumber"),
        pydantic.Field(alias="TaxFileNumber", description="The tax file number e.g 123123123."),
    ] = None
    """
    The tax file number e.g 123123123.
    """

    tax_free_threshold_claimed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="TaxFreeThresholdClaimed"),
        pydantic.Field(alias="TaxFreeThresholdClaimed", description="If tax free threshold claimed. e.g true or false"),
    ] = None
    """
    If tax free threshold claimed. e.g true or false
    """

    tax_offset_estimated_amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="TaxOffsetEstimatedAmount"),
        pydantic.Field(
            alias="TaxOffsetEstimatedAmount",
            description="If has tax offset estimated then the tax offset estimated amount. e.g 100",
        ),
    ] = None
    """
    If has tax offset estimated then the tax offset estimated amount. e.g 100
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    upward_variation_tax_withholding_amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="UpwardVariationTaxWithholdingAmount"),
        pydantic.Field(
            alias="UpwardVariationTaxWithholdingAmount",
            description="If the employee has requested that additional tax be withheld each pay run. e.g 50",
        ),
    ] = None
    """
    If the employee has requested that additional tax be withheld each pay run. e.g 50
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
