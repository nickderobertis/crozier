

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardingState(enum.StrEnum):
    """
    Onboarding state of application package
    """

    CREATED = "CREATED"
    UPLOADING = "UPLOADING"
    PROCESSING = "PROCESSING"
    ONBOARDED = "ONBOARDED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        uploading: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        onboarded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OnboardingState.CREATED:
            return created()
        if self is OnboardingState.UPLOADING:
            return uploading()
        if self is OnboardingState.PROCESSING:
            return processing()
        if self is OnboardingState.ONBOARDED:
            return onboarded()
