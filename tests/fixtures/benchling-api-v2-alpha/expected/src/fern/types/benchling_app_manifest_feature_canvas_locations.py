

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BenchlingAppManifestFeatureCanvasLocations(enum.StrEnum):
    ENTRY = "ENTRY"
    ENTRY_TEMPLATE = "ENTRY_TEMPLATE"
    APP_HOME = "APP_HOME"

    def visit(
        self,
        entry: typing.Callable[[], T_Result],
        entry_template: typing.Callable[[], T_Result],
        app_home: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BenchlingAppManifestFeatureCanvasLocations.ENTRY:
            return entry()
        if self is BenchlingAppManifestFeatureCanvasLocations.ENTRY_TEMPLATE:
            return entry_template()
        if self is BenchlingAppManifestFeatureCanvasLocations.APP_HOME:
            return app_home()
