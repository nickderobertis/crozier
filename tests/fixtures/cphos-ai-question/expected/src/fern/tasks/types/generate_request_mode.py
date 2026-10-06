

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GenerateRequestMode(enum.StrEnum):
    TOPIC_GENERATION = "topic_generation"
    LITERATURE_ADAPTATION = "literature_adaptation"
    IDEA_EXPANSION = "idea_expansion"
    PROBLEM_ENRICHMENT = "problem_enrichment"

    def visit(
        self,
        topic_generation: typing.Callable[[], T_Result],
        literature_adaptation: typing.Callable[[], T_Result],
        idea_expansion: typing.Callable[[], T_Result],
        problem_enrichment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerateRequestMode.TOPIC_GENERATION:
            return topic_generation()
        if self is GenerateRequestMode.LITERATURE_ADAPTATION:
            return literature_adaptation()
        if self is GenerateRequestMode.IDEA_EXPANSION:
            return idea_expansion()
        if self is GenerateRequestMode.PROBLEM_ENRICHMENT:
            return problem_enrichment()
