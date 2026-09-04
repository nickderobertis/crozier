

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataCategory(enum.StrEnum):
    BASIC_DATA = "basicData"
    IDENTIFICATION = "identification"
    CONTACT_INFORMATION = "contactInformation"
    ADDRESS_DATA = "addressData"
    KYC_DATA = "kycData"
    RISK_PROFILE = "riskProfile"
    COMPLIANCE_DATA = "complianceData"
    EXTENDED_DATA = "extendedData"

    def visit(
        self,
        basic_data: typing.Callable[[], T_Result],
        identification: typing.Callable[[], T_Result],
        contact_information: typing.Callable[[], T_Result],
        address_data: typing.Callable[[], T_Result],
        kyc_data: typing.Callable[[], T_Result],
        risk_profile: typing.Callable[[], T_Result],
        compliance_data: typing.Callable[[], T_Result],
        extended_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataCategory.BASIC_DATA:
            return basic_data()
        if self is DataCategory.IDENTIFICATION:
            return identification()
        if self is DataCategory.CONTACT_INFORMATION:
            return contact_information()
        if self is DataCategory.ADDRESS_DATA:
            return address_data()
        if self is DataCategory.KYC_DATA:
            return kyc_data()
        if self is DataCategory.RISK_PROFILE:
            return risk_profile()
        if self is DataCategory.COMPLIANCE_DATA:
            return compliance_data()
        if self is DataCategory.EXTENDED_DATA:
            return extended_data()
