

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CertificateSource(enum.StrEnum):
    CLOUDFRONT = "cloudfront"
    IAM = "iam"
    ACM = "acm"

    def visit(
        self,
        cloudfront: typing.Callable[[], T_Result],
        iam: typing.Callable[[], T_Result],
        acm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CertificateSource.CLOUDFRONT:
            return cloudfront()
        if self is CertificateSource.IAM:
            return iam()
        if self is CertificateSource.ACM:
            return acm()
