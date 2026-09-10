

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch400DetailsItemInvalidParameterSyntaxDescription(enum.StrEnum):
    THE_VALUE_OF_A_FIELD_DOES_NOT_CONFORM_TO_THE_EXPECTED_FORMAT = (
        "The value of a field does not conform to the expected format."
    )

    def visit(
        self, the_value_of_a_field_does_not_conform_to_the_expected_format: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is ProductsPatch400DetailsItemInvalidParameterSyntaxDescription.THE_VALUE_OF_A_FIELD_DOES_NOT_CONFORM_TO_THE_EXPECTED_FORMAT
        ):
            return the_value_of_a_field_does_not_conform_to_the_expected_format()
