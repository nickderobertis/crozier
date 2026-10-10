

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Wording(enum.StrEnum):
    BACK_ROOM = "back\\room"
    SAY_CHEESE = 'say "cheese"'
    BAKERS_DOZEN = "baker's dozen"
    NEITHER_NOR_FITS = "neither ' nor \" fits"
    CAFE = "café"
    OPEN_EVERY_WEEKDAY = "open-every-weekday"
    CLOSED_ON_HOLIDAYS = "closed-on-holidays"
    RING_BELL_FOR_SERVICE = "ring-bell-for-service"
    MIND_THE_STEP_DOWN = "mind-the-step-down"
    CASH_AND_CARD_TAKEN = "cash-and-card-taken"

    def visit(
        self,
        back_room: typing.Callable[[], T_Result],
        say_cheese: typing.Callable[[], T_Result],
        bakers_dozen: typing.Callable[[], T_Result],
        neither_nor_fits: typing.Callable[[], T_Result],
        cafe: typing.Callable[[], T_Result],
        open_every_weekday: typing.Callable[[], T_Result],
        closed_on_holidays: typing.Callable[[], T_Result],
        ring_bell_for_service: typing.Callable[[], T_Result],
        mind_the_step_down: typing.Callable[[], T_Result],
        cash_and_card_taken: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Wording.BACK_ROOM:
            return back_room()
        if self is Wording.SAY_CHEESE:
            return say_cheese()
        if self is Wording.BAKERS_DOZEN:
            return bakers_dozen()
        if self is Wording.NEITHER_NOR_FITS:
            return neither_nor_fits()
        if self is Wording.CAFE:
            return cafe()
        if self is Wording.OPEN_EVERY_WEEKDAY:
            return open_every_weekday()
        if self is Wording.CLOSED_ON_HOLIDAYS:
            return closed_on_holidays()
        if self is Wording.RING_BELL_FOR_SERVICE:
            return ring_bell_for_service()
        if self is Wording.MIND_THE_STEP_DOWN:
            return mind_the_step_down()
        if self is Wording.CASH_AND_CARD_TAKEN:
            return cash_and_card_taken()
