

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuleCriteriaExposure(enum.StrEnum):
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
        if self is RuleCriteriaExposure.PRIVATE:
            return private()
        if self is RuleCriteriaExposure.PUBLIC:
            return public()
        if self is RuleCriteriaExposure.CONDITIONAL:
            return conditional()
