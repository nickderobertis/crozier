

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewerCertificateCertificateSource(enum.StrEnum):
    """
    <note> <p>This field is deprecated. You can use one of the following: <code>[ACMCertificateArn</code>, <code>IAMCertificateId</code>, or <code>CloudFrontDefaultCertificate]</code>.</p> </note>
    """

    CLOUDFRONT = "cloudfront"
    IAM = "iam"
    ACM = "acm"

    def visit(
        self,
        cloudfront: typing.Callable[[], T_Result],
        iam: typing.Callable[[], T_Result],
        acm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViewerCertificateCertificateSource.CLOUDFRONT:
            return cloudfront()
        if self is ViewerCertificateCertificateSource.IAM:
            return iam()
        if self is ViewerCertificateCertificateSource.ACM:
            return acm()
