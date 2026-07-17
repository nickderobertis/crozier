

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiAlignmentsIndexRequestIndex(enum.StrEnum):
    CHAOTIC_NEUTRAL = "chaotic-neutral"
    CHAOTIC_EVIL = "chaotic-evil"
    CHAOTIC_GOOD = "chaotic-good"
    LAWFUL_NEUTRAL = "lawful-neutral"
    LAWFUL_EVIL = "lawful-evil"
    LAWFUL_GOOD = "lawful-good"
    NEUTRAL = "neutral"
    NEUTRAL_EVIL = "neutral-evil"
    NEUTRAL_GOOD = "neutral-good"

    def visit(
        self,
        chaotic_neutral: typing.Callable[[], T_Result],
        chaotic_evil: typing.Callable[[], T_Result],
        chaotic_good: typing.Callable[[], T_Result],
        lawful_neutral: typing.Callable[[], T_Result],
        lawful_evil: typing.Callable[[], T_Result],
        lawful_good: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
        neutral_evil: typing.Callable[[], T_Result],
        neutral_good: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiAlignmentsIndexRequestIndex.CHAOTIC_NEUTRAL:
            return chaotic_neutral()
        if self is GetApiAlignmentsIndexRequestIndex.CHAOTIC_EVIL:
            return chaotic_evil()
        if self is GetApiAlignmentsIndexRequestIndex.CHAOTIC_GOOD:
            return chaotic_good()
        if self is GetApiAlignmentsIndexRequestIndex.LAWFUL_NEUTRAL:
            return lawful_neutral()
        if self is GetApiAlignmentsIndexRequestIndex.LAWFUL_EVIL:
            return lawful_evil()
        if self is GetApiAlignmentsIndexRequestIndex.LAWFUL_GOOD:
            return lawful_good()
        if self is GetApiAlignmentsIndexRequestIndex.NEUTRAL:
            return neutral()
        if self is GetApiAlignmentsIndexRequestIndex.NEUTRAL_EVIL:
            return neutral_evil()
        if self is GetApiAlignmentsIndexRequestIndex.NEUTRAL_GOOD:
            return neutral_good()
