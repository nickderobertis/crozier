

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxpayerIdentifierType(enum.StrEnum):
    """
    A value from a MISMO prescribed list that classifies identification numbers used by the Internal Revenue Service (IRS) in the administration of tax laws. A Social Security number (SSN) is issued by the SSA; all other taxpayer identification numbers are issued by the IRS.
    """

    INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER = "IndividualTaxpayerIdentificationNumber"
    SOCIAL_SECURITY_NUMBER = "SocialSecurityNumber"

    def visit(
        self,
        individual_taxpayer_identification_number: typing.Callable[[], T_Result],
        social_security_number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaxpayerIdentifierType.INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER:
            return individual_taxpayer_identification_number()
        if self is TaxpayerIdentifierType.SOCIAL_SECURITY_NUMBER:
            return social_security_number()
