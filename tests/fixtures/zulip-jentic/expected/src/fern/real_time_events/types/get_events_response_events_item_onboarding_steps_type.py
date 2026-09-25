

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemOnboardingStepsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    ONBOARDING_STEPS = "onboarding_steps"

    def visit(self, onboarding_steps: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemOnboardingStepsType.ONBOARDING_STEPS:
            return onboarding_steps()
