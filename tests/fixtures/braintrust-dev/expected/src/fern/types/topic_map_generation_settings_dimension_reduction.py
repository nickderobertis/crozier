

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicMapGenerationSettingsDimensionReduction(enum.StrEnum):
    UMAP = "umap"
    PCA = "pca"
    NONE = "none"

    def visit(
        self,
        umap: typing.Callable[[], T_Result],
        pca: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TopicMapGenerationSettingsDimensionReduction.UMAP:
            return umap()
        if self is TopicMapGenerationSettingsDimensionReduction.PCA:
            return pca()
        if self is TopicMapGenerationSettingsDimensionReduction.NONE:
            return none()
