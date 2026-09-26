

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantCertCreateRequestReason(enum.StrEnum):
    """
    The reason the customer is exempt from sales tax.
    """

    FEDERAL_GOVERNMENT = "FederalGovernment"
    STATE_OR_LOCAL_GOVERNMENT = "StateOrLocalGovernment"
    TRIBAL_GOVERNMENT = "TribalGovernment"
    FOREIGN_DIPLOMAT = "ForeignDiplomat"
    CHARITABLE_ORGANIZATION = "CharitableOrganization"
    EDUCATIONAL_ORGANIZATION = "EducationalOrganization"
    RESALE = "Resale"
    AGRICULTURAL_PRODUCTION = "AgriculturalProduction"
    INDUSTRIAL_PRODUCTION_OR_MANUFACTURING = "IndustrialProductionOrManufacturing"
    DIRECT_PAY_PERMIT = "DirectPayPermit"
    DIRECT_MAIL = "DirectMail"
    OTHER = "Other"
    RELIGIOUS_ORGANIZATION = "ReligiousOrganization"

    def visit(
        self,
        federal_government: typing.Callable[[], T_Result],
        state_or_local_government: typing.Callable[[], T_Result],
        tribal_government: typing.Callable[[], T_Result],
        foreign_diplomat: typing.Callable[[], T_Result],
        charitable_organization: typing.Callable[[], T_Result],
        educational_organization: typing.Callable[[], T_Result],
        resale: typing.Callable[[], T_Result],
        agricultural_production: typing.Callable[[], T_Result],
        industrial_production_or_manufacturing: typing.Callable[[], T_Result],
        direct_pay_permit: typing.Callable[[], T_Result],
        direct_mail: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        religious_organization: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MerchantCertCreateRequestReason.FEDERAL_GOVERNMENT:
            return federal_government()
        if self is MerchantCertCreateRequestReason.STATE_OR_LOCAL_GOVERNMENT:
            return state_or_local_government()
        if self is MerchantCertCreateRequestReason.TRIBAL_GOVERNMENT:
            return tribal_government()
        if self is MerchantCertCreateRequestReason.FOREIGN_DIPLOMAT:
            return foreign_diplomat()
        if self is MerchantCertCreateRequestReason.CHARITABLE_ORGANIZATION:
            return charitable_organization()
        if self is MerchantCertCreateRequestReason.EDUCATIONAL_ORGANIZATION:
            return educational_organization()
        if self is MerchantCertCreateRequestReason.RESALE:
            return resale()
        if self is MerchantCertCreateRequestReason.AGRICULTURAL_PRODUCTION:
            return agricultural_production()
        if self is MerchantCertCreateRequestReason.INDUSTRIAL_PRODUCTION_OR_MANUFACTURING:
            return industrial_production_or_manufacturing()
        if self is MerchantCertCreateRequestReason.DIRECT_PAY_PERMIT:
            return direct_pay_permit()
        if self is MerchantCertCreateRequestReason.DIRECT_MAIL:
            return direct_mail()
        if self is MerchantCertCreateRequestReason.OTHER:
            return other()
        if self is MerchantCertCreateRequestReason.RELIGIOUS_ORGANIZATION:
            return religious_organization()
