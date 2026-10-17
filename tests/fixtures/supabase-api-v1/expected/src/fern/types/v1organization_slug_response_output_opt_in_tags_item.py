

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1OrganizationSlugResponseOutputOptInTagsItem(enum.StrEnum):
    AI_SQL_GENERATOR_OPT_IN = "AI_SQL_GENERATOR_OPT_IN"
    AI_DATA_GENERATOR_OPT_IN = "AI_DATA_GENERATOR_OPT_IN"
    AI_LOG_GENERATOR_OPT_IN = "AI_LOG_GENERATOR_OPT_IN"

    def visit(
        self,
        ai_sql_generator_opt_in: typing.Callable[[], T_Result],
        ai_data_generator_opt_in: typing.Callable[[], T_Result],
        ai_log_generator_opt_in: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OrganizationSlugResponseOutputOptInTagsItem.AI_SQL_GENERATOR_OPT_IN:
            return ai_sql_generator_opt_in()
        if self is V1OrganizationSlugResponseOutputOptInTagsItem.AI_DATA_GENERATOR_OPT_IN:
            return ai_data_generator_opt_in()
        if self is V1OrganizationSlugResponseOutputOptInTagsItem.AI_LOG_GENERATOR_OPT_IN:
            return ai_log_generator_opt_in()
