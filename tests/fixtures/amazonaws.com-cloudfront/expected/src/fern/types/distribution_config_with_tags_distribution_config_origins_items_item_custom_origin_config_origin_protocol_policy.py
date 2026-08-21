

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy(enum.StrEnum):
    """
    The origin protocol policy to apply to your origin.
    """

    HTTP_ONLY = "http-only"
    MATCH_VIEWER = "match-viewer"
    HTTPS_ONLY = "https-only"

    def visit(
        self,
        http_only: typing.Callable[[], T_Result],
        match_viewer: typing.Callable[[], T_Result],
        https_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy.HTTP_ONLY
        ):
            return http_only()
        if (
            self
            is DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy.MATCH_VIEWER
        ):
            return match_viewer()
        if (
            self
            is DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy.HTTPS_ONLY
        ):
            return https_only()
