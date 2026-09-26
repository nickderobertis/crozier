

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoExemptionIndicator(enum.StrEnum):
    """
    Indicates the exemption type that was applied to the authentication by the issuer, if exemption applied. Possible values:

    * **lowValue**
    * **secureCorporate**
    * **trustedBeneficiary**
    * **transactionRiskAnalysis**
    * **acquirerExemption**
    * **noExemptionApplied**
    * **visaDAFExemption**
    """

    LOW_VALUE = "lowValue"
    SECURE_CORPORATE = "secureCorporate"
    TRUSTED_BENEFICIARY = "trustedBeneficiary"
    TRANSACTION_RISK_ANALYSIS = "transactionRiskAnalysis"
    ACQUIRER_EXEMPTION = "acquirerExemption"
    NO_EXEMPTION_APPLIED = "noExemptionApplied"
    VISA_DAF_EXEMPTION = "visaDAFExemption"

    def visit(
        self,
        low_value: typing.Callable[[], T_Result],
        secure_corporate: typing.Callable[[], T_Result],
        trusted_beneficiary: typing.Callable[[], T_Result],
        transaction_risk_analysis: typing.Callable[[], T_Result],
        acquirer_exemption: typing.Callable[[], T_Result],
        no_exemption_applied: typing.Callable[[], T_Result],
        visa_daf_exemption: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationInfoExemptionIndicator.LOW_VALUE:
            return low_value()
        if self is AuthenticationInfoExemptionIndicator.SECURE_CORPORATE:
            return secure_corporate()
        if self is AuthenticationInfoExemptionIndicator.TRUSTED_BENEFICIARY:
            return trusted_beneficiary()
        if self is AuthenticationInfoExemptionIndicator.TRANSACTION_RISK_ANALYSIS:
            return transaction_risk_analysis()
        if self is AuthenticationInfoExemptionIndicator.ACQUIRER_EXEMPTION:
            return acquirer_exemption()
        if self is AuthenticationInfoExemptionIndicator.NO_EXEMPTION_APPLIED:
            return no_exemption_applied()
        if self is AuthenticationInfoExemptionIndicator.VISA_DAF_EXEMPTION:
            return visa_daf_exemption()
