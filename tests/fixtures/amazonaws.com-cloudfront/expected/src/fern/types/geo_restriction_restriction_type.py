

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GeoRestrictionRestrictionType(enum.StrEnum):
    """
    <p>The method that you want to use to restrict distribution of your content by country:</p> <ul> <li> <p> <code>none</code>: No geo restriction is enabled, meaning access to content is not restricted by client geo location.</p> </li> <li> <p> <code>blacklist</code>: The <code>Location</code> elements specify the countries in which you do not want CloudFront to distribute your content.</p> </li> <li> <p> <code>whitelist</code>: The <code>Location</code> elements specify the countries in which you want CloudFront to distribute your content.</p> </li> </ul>
    """

    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"
    NONE = "none"

    def visit(
        self,
        blacklist: typing.Callable[[], T_Result],
        whitelist: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GeoRestrictionRestrictionType.BLACKLIST:
            return blacklist()
        if self is GeoRestrictionRestrictionType.WHITELIST:
            return whitelist()
        if self is GeoRestrictionRestrictionType.NONE:
            return none()
