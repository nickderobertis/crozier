

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommunicationModelsFieldFilterType(enum.StrEnum):
    """
    Optional. The filter type. Default is HasFieldMatching.
    """

    HAS_FIELD_MATCHING = "HasFieldMatching"
    HAS_INDEX_DATA_MATCHING = "HasIndexDataMatching"
    DOES_NOT_HAVE_INDEX_DATA_MATCHING = "DoesNotHaveIndexDataMatching"

    def visit(
        self,
        has_field_matching: typing.Callable[[], T_Result],
        has_index_data_matching: typing.Callable[[], T_Result],
        does_not_have_index_data_matching: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommunicationModelsFieldFilterType.HAS_FIELD_MATCHING:
            return has_field_matching()
        if self is CommunicationModelsFieldFilterType.HAS_INDEX_DATA_MATCHING:
            return has_index_data_matching()
        if self is CommunicationModelsFieldFilterType.DOES_NOT_HAVE_INDEX_DATA_MATCHING:
            return does_not_have_index_data_matching()
