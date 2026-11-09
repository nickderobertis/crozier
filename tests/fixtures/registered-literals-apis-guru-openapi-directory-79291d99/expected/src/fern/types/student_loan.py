

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pslf_status import PslfStatus
from .servicer_address_data import ServicerAddressData
from .student_loan_status import StudentLoanStatus
from .student_repayment_plan import StudentRepaymentPlan


class StudentLoan(UniversalBaseModel):
    """
    Contains details about a student loan account
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the account that this liability belongs to.
    """

    account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number).
    """

    disbursement_dates: typing.Optional[typing.List[dt.date]] = pydantic.Field(default=None)
    """
    The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    expected_payoff_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    guarantor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The guarantor of the student loan.
    """

    interest_rate_percentage: float = pydantic.Field()
    """
    The interest rate on the loan as a percentage.
    """

    is_overdue: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if a payment is currently overdue. Availability for this field is limited.
    """

    last_payment_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the last payment.
    """

    last_payment_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    last_statement_issue_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    loan_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of loan, e.g., "Consolidation Loans".
    """

    loan_status: StudentLoanStatus
    minimum_payment_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The minimum payment due for the next billing cycle. There are some exceptions:
    Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`).
    Firstmark (`ins_116295` ) and Navient (`ins_116248`) will display as $0 if there is an autopay program in effect.
    """

    next_payment_due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    origination_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    origination_principal_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The original principal balance of the loan.
    """

    outstanding_interest_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`.
    """

    payment_reference_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match `account_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different.
    """

    pslf_status: PslfStatus
    repayment_plan: StudentRepaymentPlan
    sequence_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available.
    """

    servicer_address: ServicerAddressData
    ytd_interest_paid: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year to date (YTD) interest paid. Availability for this field is limited.
    """

    ytd_principal_paid: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year to date (YTD) principal paid. Availability for this field is limited.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
