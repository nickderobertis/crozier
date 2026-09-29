

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSubstanceStudyRequestDb(enum.StrEnum):
    CALIBRATE = "calibrate"
    ENANOMAPPER = "enanomapper"
    ENPRA = "enpra"
    MARINA = "marina"
    NANOGENOTOX = "nanogenotox"
    NANOINFORMATIX = "nanoinformatix"
    NANOREG1 = "nanoreg1"
    NANOREG2 = "nanoreg2"
    NANOTEST = "nanotest"

    def visit(
        self,
        calibrate: typing.Callable[[], T_Result],
        enanomapper: typing.Callable[[], T_Result],
        enpra: typing.Callable[[], T_Result],
        marina: typing.Callable[[], T_Result],
        nanogenotox: typing.Callable[[], T_Result],
        nanoinformatix: typing.Callable[[], T_Result],
        nanoreg1: typing.Callable[[], T_Result],
        nanoreg2: typing.Callable[[], T_Result],
        nanotest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSubstanceStudyRequestDb.CALIBRATE:
            return calibrate()
        if self is GetSubstanceStudyRequestDb.ENANOMAPPER:
            return enanomapper()
        if self is GetSubstanceStudyRequestDb.ENPRA:
            return enpra()
        if self is GetSubstanceStudyRequestDb.MARINA:
            return marina()
        if self is GetSubstanceStudyRequestDb.NANOGENOTOX:
            return nanogenotox()
        if self is GetSubstanceStudyRequestDb.NANOINFORMATIX:
            return nanoinformatix()
        if self is GetSubstanceStudyRequestDb.NANOREG1:
            return nanoreg1()
        if self is GetSubstanceStudyRequestDb.NANOREG2:
            return nanoreg2()
        if self is GetSubstanceStudyRequestDb.NANOTEST:
            return nanotest()
