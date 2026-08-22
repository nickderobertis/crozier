

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass(
    enum.StrEnum
):
    """
    A complex type that contains information about price class for this streaming distribution.
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
        if (
            self
            is CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass.PRICE_CLASS100
        ):
            return price_class100()
        if (
            self
            is CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass.PRICE_CLASS200
        ):
            return price_class200()
        if (
            self
            is CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass.PRICE_CLASS_ALL
        ):
            return price_class_all()
