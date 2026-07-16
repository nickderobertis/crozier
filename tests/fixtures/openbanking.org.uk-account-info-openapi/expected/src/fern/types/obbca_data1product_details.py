

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1product_details_fee_free_length_period import ObbcaData1ProductDetailsFeeFreeLengthPeriod
from .obbca_data1product_details_segment_item import ObbcaData1ProductDetailsSegmentItem


class ObbcaData1ProductDetails(UniversalBaseModel):
    fee_free_length: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="FeeFreeLength"),
        pydantic.Field(alias="FeeFreeLength", description="The length/duration of the fee free period"),
    ] = None
    """
    The length/duration of the fee free period
    """

    fee_free_length_period: typing_extensions.Annotated[
        typing.Optional[ObbcaData1ProductDetailsFeeFreeLengthPeriod],
        FieldMetadata(alias="FeeFreeLengthPeriod"),
        pydantic.Field(
            alias="FeeFreeLengthPeriod",
            description="The unit of period (days, weeks, months etc.) of the promotional length",
        ),
    ] = None
    """
    The unit of period (days, weeks, months etc.) of the promotional length
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Optional additional notes to supplement the Core product details"),
    ] = None
    """
    Optional additional notes to supplement the Core product details
    """

    segment: typing_extensions.Annotated[
        typing.Optional[typing.List[ObbcaData1ProductDetailsSegmentItem]],
        FieldMetadata(alias="Segment"),
        pydantic.Field(
            alias="Segment",
            description="Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.\n\nRead more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd \nWith respect to BCA products, they are segmented in relation to different markets that they wish to focus on. ",
        ),
    ] = None
    """
    Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.
    
    Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd 
    With respect to BCA products, they are segmented in relation to different markets that they wish to focus on. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
