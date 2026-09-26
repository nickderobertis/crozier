

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MerchantCertCreateRequestCustomerBusinessType(enum.StrEnum):
    """
    The type of business the customer is.
    """

    ACCOMMODATION_AND_FOOD_SERVICES = "AccommodationAndFoodServices"
    AGRICULTURAL_FORESTRY_FISHING_HUNTING = "AgriculturalForestryFishingHunting"
    CONSTRUCTION = "Construction"
    FINANCE_AND_INSURANCE = "FinanceAndInsurance"
    INFORMATION_PUBLISHING_AND_COMMUNICATIONS = "InformationPublishingAndCommunications"
    MANUFACTURING = "Manufacturing"
    MINING = "Mining"
    REAL_ESTATE = "RealEstate"
    RENTAL_AND_LEASING = "RentalAndLeasing"
    RETAIL_TRADE = "RetailTrade"
    TRANSPORTATION_AND_WAREHOUSING = "TransportationAndWarehousing"
    UTILITIES = "Utilities"
    WHOLESALE_TRADE = "WholesaleTrade"
    BUSINESS_SERVICES = "BusinessServices"
    PROFESSIONAL_SERVICES = "ProfessionalServices"
    EDUCATION_AND_HEALTH_CARE_SERVICES = "EducationAndHealthCareServices"
    NONPROFIT_ORGANIZATION = "NonprofitOrganization"
    GOVERNMENT = "Government"
    NOT_A_BUSINESS = "NotABusiness"
    OTHER = "Other"

    def visit(
        self,
        accommodation_and_food_services: typing.Callable[[], T_Result],
        agricultural_forestry_fishing_hunting: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        finance_and_insurance: typing.Callable[[], T_Result],
        information_publishing_and_communications: typing.Callable[[], T_Result],
        manufacturing: typing.Callable[[], T_Result],
        mining: typing.Callable[[], T_Result],
        real_estate: typing.Callable[[], T_Result],
        rental_and_leasing: typing.Callable[[], T_Result],
        retail_trade: typing.Callable[[], T_Result],
        transportation_and_warehousing: typing.Callable[[], T_Result],
        utilities: typing.Callable[[], T_Result],
        wholesale_trade: typing.Callable[[], T_Result],
        business_services: typing.Callable[[], T_Result],
        professional_services: typing.Callable[[], T_Result],
        education_and_health_care_services: typing.Callable[[], T_Result],
        nonprofit_organization: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
        not_a_business: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MerchantCertCreateRequestCustomerBusinessType.ACCOMMODATION_AND_FOOD_SERVICES:
            return accommodation_and_food_services()
        if self is MerchantCertCreateRequestCustomerBusinessType.AGRICULTURAL_FORESTRY_FISHING_HUNTING:
            return agricultural_forestry_fishing_hunting()
        if self is MerchantCertCreateRequestCustomerBusinessType.CONSTRUCTION:
            return construction()
        if self is MerchantCertCreateRequestCustomerBusinessType.FINANCE_AND_INSURANCE:
            return finance_and_insurance()
        if self is MerchantCertCreateRequestCustomerBusinessType.INFORMATION_PUBLISHING_AND_COMMUNICATIONS:
            return information_publishing_and_communications()
        if self is MerchantCertCreateRequestCustomerBusinessType.MANUFACTURING:
            return manufacturing()
        if self is MerchantCertCreateRequestCustomerBusinessType.MINING:
            return mining()
        if self is MerchantCertCreateRequestCustomerBusinessType.REAL_ESTATE:
            return real_estate()
        if self is MerchantCertCreateRequestCustomerBusinessType.RENTAL_AND_LEASING:
            return rental_and_leasing()
        if self is MerchantCertCreateRequestCustomerBusinessType.RETAIL_TRADE:
            return retail_trade()
        if self is MerchantCertCreateRequestCustomerBusinessType.TRANSPORTATION_AND_WAREHOUSING:
            return transportation_and_warehousing()
        if self is MerchantCertCreateRequestCustomerBusinessType.UTILITIES:
            return utilities()
        if self is MerchantCertCreateRequestCustomerBusinessType.WHOLESALE_TRADE:
            return wholesale_trade()
        if self is MerchantCertCreateRequestCustomerBusinessType.BUSINESS_SERVICES:
            return business_services()
        if self is MerchantCertCreateRequestCustomerBusinessType.PROFESSIONAL_SERVICES:
            return professional_services()
        if self is MerchantCertCreateRequestCustomerBusinessType.EDUCATION_AND_HEALTH_CARE_SERVICES:
            return education_and_health_care_services()
        if self is MerchantCertCreateRequestCustomerBusinessType.NONPROFIT_ORGANIZATION:
            return nonprofit_organization()
        if self is MerchantCertCreateRequestCustomerBusinessType.GOVERNMENT:
            return government()
        if self is MerchantCertCreateRequestCustomerBusinessType.NOT_A_BUSINESS:
            return not_a_business()
        if self is MerchantCertCreateRequestCustomerBusinessType.OTHER:
            return other()
