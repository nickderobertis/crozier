

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuleModelDataCriteriaExposure(enum.StrEnum):
    """
    File exposure
    """

    PRIVATE = "private"
    PUBLIC = "public"
    CONDITIONAL = "conditional"

    def visit(
        self,
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        conditional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuleModelDataCriteriaExposure.PRIVATE:
            return private()
        if self is RuleModelDataCriteriaExposure.PUBLIC:
            return public()
        if self is RuleModelDataCriteriaExposure.CONDITIONAL:
            return conditional()
