

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType(enum.StrEnum):
    """
    <p>Specifies the event type that triggers a Lambda function invocation. Valid values are:</p> <ul> <li> <p> <code>viewer-request</code> </p> </li> <li> <p> <code>origin-request</code> </p> </li> <li> <p> <code>viewer-response</code> </p> </li> <li> <p> <code>origin-response</code> </p> </li> </ul>
    """

    VIEWER_REQUEST = "viewer-request"
    VIEWER_RESPONSE = "viewer-response"
    ORIGIN_REQUEST = "origin-request"
    ORIGIN_RESPONSE = "origin-response"

    def visit(
        self,
        viewer_request: typing.Callable[[], T_Result],
        viewer_response: typing.Callable[[], T_Result],
        origin_request: typing.Callable[[], T_Result],
        origin_response: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType.VIEWER_REQUEST:
            return viewer_request()
        if self is DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType.VIEWER_RESPONSE:
            return viewer_response()
        if self is DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType.ORIGIN_REQUEST:
            return origin_request()
        if self is DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType.ORIGIN_RESPONSE:
            return origin_response()
