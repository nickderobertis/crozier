

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonsterAlignments(enum.StrEnum):
    """
    A creature's general moral and personal attitudes.
    """

    CHAOTIC_NEUTRAL = "chaotic neutral"
    CHAOTIC_EVIL = "chaotic evil"
    CHAOTIC_GOOD = "chaotic good"
    LAWFUL_NEUTRAL = "lawful neutral"
    LAWFUL_EVIL = "lawful evil"
    LAWFUL_GOOD = "lawful good"
    NEUTRAL = "neutral"
    NEUTRAL_EVIL = "neutral evil"
    NEUTRAL_GOOD = "neutral good"
    ANY_ALIGNMENT = "any alignment"
    UNALIGNED = "unaligned"

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
        any_alignment: typing.Callable[[], T_Result],
        unaligned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonsterAlignments.CHAOTIC_NEUTRAL:
            return chaotic_neutral()
        if self is MonsterAlignments.CHAOTIC_EVIL:
            return chaotic_evil()
        if self is MonsterAlignments.CHAOTIC_GOOD:
            return chaotic_good()
        if self is MonsterAlignments.LAWFUL_NEUTRAL:
            return lawful_neutral()
        if self is MonsterAlignments.LAWFUL_EVIL:
            return lawful_evil()
        if self is MonsterAlignments.LAWFUL_GOOD:
            return lawful_good()
        if self is MonsterAlignments.NEUTRAL:
            return neutral()
        if self is MonsterAlignments.NEUTRAL_EVIL:
            return neutral_evil()
        if self is MonsterAlignments.NEUTRAL_GOOD:
            return neutral_good()
        if self is MonsterAlignments.ANY_ALIGNMENT:
            return any_alignment()
        if self is MonsterAlignments.UNALIGNED:
            return unaligned()
