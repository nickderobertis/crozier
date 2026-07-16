

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemProductType(str, enum.Enum):
    """
    Product type : Personal Current Account, Business Current Account
    """

    BUSINESS_CURRENT_ACCOUNT = "BusinessCurrentAccount"
    COMMERCIAL_CREDIT_CARD = "CommercialCreditCard"
    OTHER = "Other"
    PERSONAL_CURRENT_ACCOUNT = "PersonalCurrentAccount"
    SME_LOAN = "SMELoan"

    def visit(
        self,
        business_current_account: typing.Callable[[], T_Result],
        commercial_credit_card: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        personal_current_account: typing.Callable[[], T_Result],
        sme_loan: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemProductType.BUSINESS_CURRENT_ACCOUNT:
            return business_current_account()
        if self is ObReadProduct2DataProductItemProductType.COMMERCIAL_CREDIT_CARD:
            return commercial_credit_card()
        if self is ObReadProduct2DataProductItemProductType.OTHER:
            return other()
        if self is ObReadProduct2DataProductItemProductType.PERSONAL_CURRENT_ACCOUNT:
            return personal_current_account()
        if self is ObReadProduct2DataProductItemProductType.SME_LOAN:
            return sme_loan()
