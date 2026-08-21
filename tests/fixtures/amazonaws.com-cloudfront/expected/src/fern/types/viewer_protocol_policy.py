

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewerProtocolPolicy(enum.StrEnum):
    ALLOW_ALL = "allow-all"
    HTTPS_ONLY = "https-only"
    REDIRECT_TO_HTTPS = "redirect-to-https"

    def visit(
        self,
        allow_all: typing.Callable[[], T_Result],
        https_only: typing.Callable[[], T_Result],
        redirect_to_https: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViewerProtocolPolicy.ALLOW_ALL:
            return allow_all()
        if self is ViewerProtocolPolicy.HTTPS_ONLY:
            return https_only()
        if self is ViewerProtocolPolicy.REDIRECT_TO_HTTPS:
            return redirect_to_https()
