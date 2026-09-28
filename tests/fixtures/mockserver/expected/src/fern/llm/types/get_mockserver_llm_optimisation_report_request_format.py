

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMockserverLlmOptimisationReportRequestFormat(enum.StrEnum):
    JSON = "json"
    MARKDOWN = "markdown"
    CSV = "csv"
    OPENAI_EVALS = "openai-evals"
    FINE_TUNE = "fine-tune"
    PROMPTFOO = "promptfoo"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
        openai_evals: typing.Callable[[], T_Result],
        fine_tune: typing.Callable[[], T_Result],
        promptfoo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMockserverLlmOptimisationReportRequestFormat.JSON:
            return json()
        if self is GetMockserverLlmOptimisationReportRequestFormat.MARKDOWN:
            return markdown()
        if self is GetMockserverLlmOptimisationReportRequestFormat.CSV:
            return csv()
        if self is GetMockserverLlmOptimisationReportRequestFormat.OPENAI_EVALS:
            return openai_evals()
        if self is GetMockserverLlmOptimisationReportRequestFormat.FINE_TUNE:
            return fine_tune()
        if self is GetMockserverLlmOptimisationReportRequestFormat.PROMPTFOO:
            return promptfoo()
