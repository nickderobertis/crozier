

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1ProductDetailsSegmentItem(enum.StrEnum):
    """
    Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.

    Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd
    With respect to BCA products, they are segmented in relation to different markets that they wish to focus on.
    """

    CLIENT_ACCOUNT = "ClientAccount"
    STANDARD = "Standard"
    NON_COMMERCIAL_CHAITIES_CLB_SOC = "NonCommercialChaitiesClbSoc"
    NON_COMMERCIAL_PUBLIC_AUTH_GOVT = "NonCommercialPublicAuthGovt"
    RELIGIOUS = "Religious"
    SECTOR_SPECIFIC = "SectorSpecific"
    STARTUP = "Startup"
    SWITCHER = "Switcher"

    def visit(
        self,
        client_account: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        non_commercial_chaities_clb_soc: typing.Callable[[], T_Result],
        non_commercial_public_auth_govt: typing.Callable[[], T_Result],
        religious: typing.Callable[[], T_Result],
        sector_specific: typing.Callable[[], T_Result],
        startup: typing.Callable[[], T_Result],
        switcher: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1ProductDetailsSegmentItem.CLIENT_ACCOUNT:
            return client_account()
        if self is ObbcaData1ProductDetailsSegmentItem.STANDARD:
            return standard()
        if self is ObbcaData1ProductDetailsSegmentItem.NON_COMMERCIAL_CHAITIES_CLB_SOC:
            return non_commercial_chaities_clb_soc()
        if self is ObbcaData1ProductDetailsSegmentItem.NON_COMMERCIAL_PUBLIC_AUTH_GOVT:
            return non_commercial_public_auth_govt()
        if self is ObbcaData1ProductDetailsSegmentItem.RELIGIOUS:
            return religious()
        if self is ObbcaData1ProductDetailsSegmentItem.SECTOR_SPECIFIC:
            return sector_specific()
        if self is ObbcaData1ProductDetailsSegmentItem.STARTUP:
            return startup()
        if self is ObbcaData1ProductDetailsSegmentItem.SWITCHER:
            return switcher()
