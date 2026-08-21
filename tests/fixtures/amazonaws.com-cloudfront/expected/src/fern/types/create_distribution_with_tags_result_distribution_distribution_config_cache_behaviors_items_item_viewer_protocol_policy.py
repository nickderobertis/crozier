

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy(
    enum.StrEnum
):
    """
    <p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL. </p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden). </p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html">Using an HTTPS Connection to Access Your Objects</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>
    """

    ALLOW_ALL = "allow-all"
    HTTPS_ONLY = "https-only"
    REDIRECT_TO_HTTPS = "redirect-to-https"

    def visit(
        self,
        allow_all: typing.Callable[[], T_Result],
        https_only: typing.Callable[[], T_Result],
        redirect_to_https: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy.ALLOW_ALL
        ):
            return allow_all()
        if (
            self
            is CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy.HTTPS_ONLY
        ):
            return https_only()
        if (
            self
            is CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy.REDIRECT_TO_HTTPS
        ):
            return redirect_to_https()
