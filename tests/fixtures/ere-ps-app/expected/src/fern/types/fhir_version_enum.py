

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FhirVersionEnum(enum.StrEnum):
    DSTU2 = "DSTU2"
    DSTU2HL7ORG = "DSTU2_HL7ORG"
    DSTU21 = "DSTU2_1"
    DSTU3 = "DSTU3"
    R4 = "R4"
    R4B = "R4B"
    R5 = "R5"

    def visit(
        self,
        dstu2: typing.Callable[[], T_Result],
        dstu2hl7org: typing.Callable[[], T_Result],
        dstu21: typing.Callable[[], T_Result],
        dstu3: typing.Callable[[], T_Result],
        r4: typing.Callable[[], T_Result],
        r4b: typing.Callable[[], T_Result],
        r5: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FhirVersionEnum.DSTU2:
            return dstu2()
        if self is FhirVersionEnum.DSTU2HL7ORG:
            return dstu2hl7org()
        if self is FhirVersionEnum.DSTU21:
            return dstu21()
        if self is FhirVersionEnum.DSTU3:
            return dstu3()
        if self is FhirVersionEnum.R4:
            return r4()
        if self is FhirVersionEnum.R4B:
            return r4b()
        if self is FhirVersionEnum.R5:
            return r5()
