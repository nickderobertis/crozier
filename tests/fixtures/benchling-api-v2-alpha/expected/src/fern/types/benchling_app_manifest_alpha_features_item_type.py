

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BenchlingAppManifestAlphaFeaturesItemType(enum.StrEnum):
    """
    The feature type controls where in the UI a Canvas associated with this feature is rendered.
    """

    APP_HOMEPAGE = "APP_HOMEPAGE"

    def visit(self, app_homepage: typing.Callable[[], T_Result]) -> T_Result:
        if self is BenchlingAppManifestAlphaFeaturesItemType.APP_HOMEPAGE:
            return app_homepage()
