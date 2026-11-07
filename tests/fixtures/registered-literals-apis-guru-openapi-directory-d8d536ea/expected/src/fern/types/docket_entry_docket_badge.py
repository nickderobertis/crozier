

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocketEntryDocketBadge(enum.StrEnum):
    """
    Docket Badge helps you to know what type of a docket entry it is.
    """

    DOCKET = "DOCKET"
    CHARGE = "CHARGE"
    HEARING = "HEARING"
    JUDGEMENT = "JUDGEMENT"
    FINANCIAL = "FINANCIAL"
    DISPOSITION = "DISPOSITION"
    SENTENCE = "SENTENCE"
    BOND = "BOND"
    BAIL = "BAIL"
    CAUSE_OF_ACTION = "CAUSE_OF_ACTION"
    ARREST = "ARREST"
    WARRANT = "WARRANT"
    SUMMON = "SUMMON"
    TICKLER = "TICKLER"
    OPINION = "OPINION"

    def visit(
        self,
        docket: typing.Callable[[], T_Result],
        charge: typing.Callable[[], T_Result],
        hearing: typing.Callable[[], T_Result],
        judgement: typing.Callable[[], T_Result],
        financial: typing.Callable[[], T_Result],
        disposition: typing.Callable[[], T_Result],
        sentence: typing.Callable[[], T_Result],
        bond: typing.Callable[[], T_Result],
        bail: typing.Callable[[], T_Result],
        cause_of_action: typing.Callable[[], T_Result],
        arrest: typing.Callable[[], T_Result],
        warrant: typing.Callable[[], T_Result],
        summon: typing.Callable[[], T_Result],
        tickler: typing.Callable[[], T_Result],
        opinion: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocketEntryDocketBadge.DOCKET:
            return docket()
        if self is DocketEntryDocketBadge.CHARGE:
            return charge()
        if self is DocketEntryDocketBadge.HEARING:
            return hearing()
        if self is DocketEntryDocketBadge.JUDGEMENT:
            return judgement()
        if self is DocketEntryDocketBadge.FINANCIAL:
            return financial()
        if self is DocketEntryDocketBadge.DISPOSITION:
            return disposition()
        if self is DocketEntryDocketBadge.SENTENCE:
            return sentence()
        if self is DocketEntryDocketBadge.BOND:
            return bond()
        if self is DocketEntryDocketBadge.BAIL:
            return bail()
        if self is DocketEntryDocketBadge.CAUSE_OF_ACTION:
            return cause_of_action()
        if self is DocketEntryDocketBadge.ARREST:
            return arrest()
        if self is DocketEntryDocketBadge.WARRANT:
            return warrant()
        if self is DocketEntryDocketBadge.SUMMON:
            return summon()
        if self is DocketEntryDocketBadge.TICKLER:
            return tickler()
        if self is DocketEntryDocketBadge.OPINION:
            return opinion()
