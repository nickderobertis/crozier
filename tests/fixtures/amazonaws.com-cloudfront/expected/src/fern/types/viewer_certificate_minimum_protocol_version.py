

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewerCertificateMinimumProtocolVersion(enum.StrEnum):
    """
    <p>Specify the minimum version of the SSL/TLS protocol that you want CloudFront to use for HTTPS connections between viewers and CloudFront: <code>SSLv3</code> or <code>TLSv1</code>. CloudFront serves your objects only to viewers that support SSL/TLS version that you specify and later versions. The <code>TLSv1</code> protocol is more secure, so we recommend that you specify <code>SSLv3</code> only if your users are using browsers or devices that don't support <code>TLSv1</code>. Note the following:</p> <ul> <li> <p>If you specify &lt;CloudFrontDefaultCertificate&gt;true&lt;CloudFrontDefaultCertificate&gt;, the minimum SSL protocol version is <code>TLSv1</code> and can't be changed.</p> </li> <li> <p>If you're using a custom certificate (if you specify a value for <code>ACMCertificateArn</code> or for <code>IAMCertificateId</code>) and if you're using SNI (if you specify <code>sni-only</code> for <code>SSLSupportMethod</code>), you must specify <code>TLSv1</code> for <code>MinimumProtocolVersion</code>.</p> </li> </ul>
    """

    SS_LV3 = "SSLv3"
    TL_SV1 = "TLSv1"

    def visit(self, ss_lv3: typing.Callable[[], T_Result], tl_sv1: typing.Callable[[], T_Result]) -> T_Result:
        if self is ViewerCertificateMinimumProtocolVersion.SS_LV3:
            return ss_lv3()
        if self is ViewerCertificateMinimumProtocolVersion.TL_SV1:
            return tl_sv1()
