

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamSpecialization(enum.StrEnum):
    NONE = "none"
    EDUCATION_STANDARD = "educationStandard"
    EDUCATION_CLASS = "educationClass"
    EDUCATION_PROFESSIONAL_LEARNING_COMMUNITY = "educationProfessionalLearningCommunity"
    EDUCATION_STAFF = "educationStaff"
    HEALTHCARE_STANDARD = "healthcareStandard"
    HEALTHCARE_CARE_COORDINATION = "healthcareCareCoordination"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        education_standard: typing.Callable[[], T_Result],
        education_class: typing.Callable[[], T_Result],
        education_professional_learning_community: typing.Callable[[], T_Result],
        education_staff: typing.Callable[[], T_Result],
        healthcare_standard: typing.Callable[[], T_Result],
        healthcare_care_coordination: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TeamSpecialization.NONE:
            return none()
        if self is TeamSpecialization.EDUCATION_STANDARD:
            return education_standard()
        if self is TeamSpecialization.EDUCATION_CLASS:
            return education_class()
        if self is TeamSpecialization.EDUCATION_PROFESSIONAL_LEARNING_COMMUNITY:
            return education_professional_learning_community()
        if self is TeamSpecialization.EDUCATION_STAFF:
            return education_staff()
        if self is TeamSpecialization.HEALTHCARE_STANDARD:
            return healthcare_standard()
        if self is TeamSpecialization.HEALTHCARE_CARE_COORDINATION:
            return healthcare_care_coordination()
        if self is TeamSpecialization.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
