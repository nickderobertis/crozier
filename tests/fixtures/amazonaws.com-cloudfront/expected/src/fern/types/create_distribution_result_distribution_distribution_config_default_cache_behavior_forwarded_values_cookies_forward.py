

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward(
    enum.StrEnum
):
    """
    <p>Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the <code>WhitelistedNames</code> complex type.</p> <p>Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the <code>Forward</code> element. </p>
    """

    NONE = "none"
    WHITELIST = "whitelist"
    ALL = "all"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        whitelist: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward.NONE
        ):
            return none()
        if (
            self
            is CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward.WHITELIST
        ):
            return whitelist()
        if (
            self
            is CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward.ALL
        ):
            return all_()
