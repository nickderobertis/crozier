

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1ProductDetailsSegmentItem(enum.StrEnum):
    """
    Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.

    Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd
    With respect to PCA products, they are segmented in relation to different markets that they wish to focus on.
    """

    BASIC = "Basic"
    BENEFIT_AND_REWARD = "BenefitAndReward"
    CREDIT_INTEREST = "CreditInterest"
    CASHBACK = "Cashback"
    GENERAL = "General"
    GRADUATE = "Graduate"
    OTHER = "Other"
    OVERDRAFT = "Overdraft"
    PACKAGED = "Packaged"
    PREMIUM = "Premium"
    REWARD = "Reward"
    STUDENT = "Student"
    YOUNG_ADULT = "YoungAdult"
    YOUTH = "Youth"

    def visit(
        self,
        basic: typing.Callable[[], T_Result],
        benefit_and_reward: typing.Callable[[], T_Result],
        credit_interest: typing.Callable[[], T_Result],
        cashback: typing.Callable[[], T_Result],
        general: typing.Callable[[], T_Result],
        graduate: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        overdraft: typing.Callable[[], T_Result],
        packaged: typing.Callable[[], T_Result],
        premium: typing.Callable[[], T_Result],
        reward: typing.Callable[[], T_Result],
        student: typing.Callable[[], T_Result],
        young_adult: typing.Callable[[], T_Result],
        youth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1ProductDetailsSegmentItem.BASIC:
            return basic()
        if self is ObpcaData1ProductDetailsSegmentItem.BENEFIT_AND_REWARD:
            return benefit_and_reward()
        if self is ObpcaData1ProductDetailsSegmentItem.CREDIT_INTEREST:
            return credit_interest()
        if self is ObpcaData1ProductDetailsSegmentItem.CASHBACK:
            return cashback()
        if self is ObpcaData1ProductDetailsSegmentItem.GENERAL:
            return general()
        if self is ObpcaData1ProductDetailsSegmentItem.GRADUATE:
            return graduate()
        if self is ObpcaData1ProductDetailsSegmentItem.OTHER:
            return other()
        if self is ObpcaData1ProductDetailsSegmentItem.OVERDRAFT:
            return overdraft()
        if self is ObpcaData1ProductDetailsSegmentItem.PACKAGED:
            return packaged()
        if self is ObpcaData1ProductDetailsSegmentItem.PREMIUM:
            return premium()
        if self is ObpcaData1ProductDetailsSegmentItem.REWARD:
            return reward()
        if self is ObpcaData1ProductDetailsSegmentItem.STUDENT:
            return student()
        if self is ObpcaData1ProductDetailsSegmentItem.YOUNG_ADULT:
            return young_adult()
        if self is ObpcaData1ProductDetailsSegmentItem.YOUTH:
            return youth()
