

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidationResponsePropertiesStatus(enum.StrEnum):
    """
    Overall validation status.
    """

    ALL_VALID_TO_PROCEED = "AllValidToProceed"
    INPUTS_REVISIT_REQUIRED = "InputsRevisitRequired"
    CERTAIN_INPUT_VALIDATIONS_SKIPPED = "CertainInputValidationsSkipped"

    def visit(
        self,
        all_valid_to_proceed: typing.Callable[[], T_Result],
        inputs_revisit_required: typing.Callable[[], T_Result],
        certain_input_validations_skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValidationResponsePropertiesStatus.ALL_VALID_TO_PROCEED:
            return all_valid_to_proceed()
        if self is ValidationResponsePropertiesStatus.INPUTS_REVISIT_REQUIRED:
            return inputs_revisit_required()
        if self is ValidationResponsePropertiesStatus.CERTAIN_INPUT_VALIDATIONS_SKIPPED:
            return certain_input_validations_skipped()
