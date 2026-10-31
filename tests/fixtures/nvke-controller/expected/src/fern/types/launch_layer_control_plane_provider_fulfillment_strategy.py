

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchLayerControlPlaneProviderFulfillmentStrategy(enum.StrEnum):
    """
    Controls how the Compute Allocation Operator places the request.
    """

    BEST_EFFORT = "BEST_EFFORT"
    ALL_OR_NOTHING = "ALL_OR_NOTHING"
    WAIT_FOR_RESOURCE = "WAIT_FOR_RESOURCE"

    def visit(
        self,
        best_effort: typing.Callable[[], T_Result],
        all_or_nothing: typing.Callable[[], T_Result],
        wait_for_resource: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LaunchLayerControlPlaneProviderFulfillmentStrategy.BEST_EFFORT:
            return best_effort()
        if self is LaunchLayerControlPlaneProviderFulfillmentStrategy.ALL_OR_NOTHING:
            return all_or_nothing()
        if self is LaunchLayerControlPlaneProviderFulfillmentStrategy.WAIT_FOR_RESOURCE:
            return wait_for_resource()
