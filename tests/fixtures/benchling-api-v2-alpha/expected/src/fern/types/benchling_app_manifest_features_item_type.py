

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BenchlingAppManifestFeaturesItemType(enum.StrEnum):
    """
    The feature type controls where in the UI a Canvas associated with this feature is rendered.
    """

    APP_HOMEPAGE = "APP_HOMEPAGE"
    ASSAY_RUN = "ASSAY_RUN"
    CANVAS = "CANVAS"

    def visit(
        self,
        app_homepage: typing.Callable[[], T_Result],
        assay_run: typing.Callable[[], T_Result],
        canvas: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BenchlingAppManifestFeaturesItemType.APP_HOMEPAGE:
            return app_homepage()
        if self is BenchlingAppManifestFeaturesItemType.ASSAY_RUN:
            return assay_run()
        if self is BenchlingAppManifestFeaturesItemType.CANVAS:
            return canvas()
