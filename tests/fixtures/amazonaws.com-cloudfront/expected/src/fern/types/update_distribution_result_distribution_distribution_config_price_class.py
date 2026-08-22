

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateDistributionResultDistributionDistributionConfigPriceClass(enum.StrEnum):
    """
    <p>The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify <code>PriceClass_All</code>, CloudFront responds to requests for your objects from all CloudFront edge locations.</p> <p>If you specify a price class other than <code>PriceClass_All</code>, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.</p> <p>For more information about price classes, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html">Choosing the Price Class for a CloudFront Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>. For information about CloudFront pricing, including how price classes map to CloudFront regions, see <a href="https://aws.amazon.com/cloudfront/pricing/">Amazon CloudFront Pricing</a>.</p>
    """

    PRICE_CLASS100 = "PriceClass_100"
    PRICE_CLASS200 = "PriceClass_200"
    PRICE_CLASS_ALL = "PriceClass_All"

    def visit(
        self,
        price_class100: typing.Callable[[], T_Result],
        price_class200: typing.Callable[[], T_Result],
        price_class_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateDistributionResultDistributionDistributionConfigPriceClass.PRICE_CLASS100:
            return price_class100()
        if self is UpdateDistributionResultDistributionDistributionConfigPriceClass.PRICE_CLASS200:
            return price_class200()
        if self is UpdateDistributionResultDistributionDistributionConfigPriceClass.PRICE_CLASS_ALL:
            return price_class_all()
