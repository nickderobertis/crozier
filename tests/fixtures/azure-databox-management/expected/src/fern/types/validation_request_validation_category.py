

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidationRequestValidationCategory(enum.StrEnum):
    """
    Identify the nature of validation.
    """

    JOB_CREATION_VALIDATION = "JobCreationValidation"

    def visit(self, job_creation_validation: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValidationRequestValidationCategory.JOB_CREATION_VALIDATION:
            return job_creation_validation()
