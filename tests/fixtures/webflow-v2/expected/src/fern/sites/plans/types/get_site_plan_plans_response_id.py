

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetSitePlanPlansResponseId(enum.StrEnum):
    """
    ID of the hosting plan.
    """

    HOSTING_BASIC_V3 = "hosting-basic-v3"
    HOSTING_CMS_V3 = "hosting-cms-v3"
    HOSTING_BUSINESS_V3 = "hosting-business-v3"
    HOSTING_ECOMMERCE_STANDARD_V2 = "hosting-ecommerce-standard-v2"
    HOSTING_ECOMMERCE_PLUS_V2 = "hosting-ecommerce-plus-v2"
    HOSTING_ECOMMERCE_ADVANCED_V2 = "hosting-ecommerce-advanced-v2"
    HOSTING_BASIC_V4 = "hosting-basic-v4"
    HOSTING_CMS_V4 = "hosting-cms-v4"
    HOSTING_BUSINESS_V4 = "hosting-business-v4"
    HOSTING_ECOMMERCE_STANDARD_V3 = "hosting-ecommerce-standard-v3"
    HOSTING_ECOMMERCE_PLUS_V3 = "hosting-ecommerce-plus-v3"
    HOSTING_ECOMMERCE_ADVANCED_V3 = "hosting-ecommerce-advanced-v3"

    def visit(
        self,
        hosting_basic_v3: typing.Callable[[], T_Result],
        hosting_cms_v3: typing.Callable[[], T_Result],
        hosting_business_v3: typing.Callable[[], T_Result],
        hosting_ecommerce_standard_v2: typing.Callable[[], T_Result],
        hosting_ecommerce_plus_v2: typing.Callable[[], T_Result],
        hosting_ecommerce_advanced_v2: typing.Callable[[], T_Result],
        hosting_basic_v4: typing.Callable[[], T_Result],
        hosting_cms_v4: typing.Callable[[], T_Result],
        hosting_business_v4: typing.Callable[[], T_Result],
        hosting_ecommerce_standard_v3: typing.Callable[[], T_Result],
        hosting_ecommerce_plus_v3: typing.Callable[[], T_Result],
        hosting_ecommerce_advanced_v3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSitePlanPlansResponseId.HOSTING_BASIC_V3:
            return hosting_basic_v3()
        if self is GetSitePlanPlansResponseId.HOSTING_CMS_V3:
            return hosting_cms_v3()
        if self is GetSitePlanPlansResponseId.HOSTING_BUSINESS_V3:
            return hosting_business_v3()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_STANDARD_V2:
            return hosting_ecommerce_standard_v2()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_PLUS_V2:
            return hosting_ecommerce_plus_v2()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_ADVANCED_V2:
            return hosting_ecommerce_advanced_v2()
        if self is GetSitePlanPlansResponseId.HOSTING_BASIC_V4:
            return hosting_basic_v4()
        if self is GetSitePlanPlansResponseId.HOSTING_CMS_V4:
            return hosting_cms_v4()
        if self is GetSitePlanPlansResponseId.HOSTING_BUSINESS_V4:
            return hosting_business_v4()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_STANDARD_V3:
            return hosting_ecommerce_standard_v3()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_PLUS_V3:
            return hosting_ecommerce_plus_v3()
        if self is GetSitePlanPlansResponseId.HOSTING_ECOMMERCE_ADVANCED_V3:
            return hosting_ecommerce_advanced_v3()
