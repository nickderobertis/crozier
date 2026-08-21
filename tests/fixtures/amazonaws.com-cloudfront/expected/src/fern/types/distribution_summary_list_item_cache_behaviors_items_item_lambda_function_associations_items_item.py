

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
    DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
)


class DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem(UniversalBaseModel):
    """
    A complex type that contains a Lambda function association.
    """

    lambda_function_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LambdaFunctionARN"),
        pydantic.Field(alias="LambdaFunctionARN", description="The ARN of the Lambda function."),
    ] = None
    """
    The ARN of the Lambda function.
    """

    event_type: typing_extensions.Annotated[
        typing.Optional[DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType],
        FieldMetadata(alias="EventType"),
        pydantic.Field(
            alias="EventType",
            description="<p>Specifies the event type that triggers a Lambda function invocation. Valid values are:</p> <ul> <li> <p> <code>viewer-request</code> </p> </li> <li> <p> <code>origin-request</code> </p> </li> <li> <p> <code>viewer-response</code> </p> </li> <li> <p> <code>origin-response</code> </p> </li> </ul>",
        ),
    ] = None
    """
    <p>Specifies the event type that triggers a Lambda function invocation. Valid values are:</p> <ul> <li> <p> <code>viewer-request</code> </p> </li> <li> <p> <code>origin-request</code> </p> </li> <li> <p> <code>viewer-response</code> </p> </li> <li> <p> <code>origin-response</code> </p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
