

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldQuestionType(enum.StrEnum):
    """
    Block types that produce answer values and can be referenced as field sources.
    """

    INPUT_TEXT = "INPUT_TEXT"
    INPUT_NUMBER = "INPUT_NUMBER"
    INPUT_EMAIL = "INPUT_EMAIL"
    INPUT_LINK = "INPUT_LINK"
    INPUT_PHONE_NUMBER = "INPUT_PHONE_NUMBER"
    INPUT_DATE = "INPUT_DATE"
    INPUT_TIME = "INPUT_TIME"
    TEXTAREA = "TEXTAREA"
    RATING = "RATING"
    LINEAR_SCALE = "LINEAR_SCALE"
    CHECKBOX = "CHECKBOX"
    MULTIPLE_CHOICE_OPTION = "MULTIPLE_CHOICE_OPTION"
    DROPDOWN_OPTION = "DROPDOWN_OPTION"
    RANKING_OPTION = "RANKING_OPTION"
    MULTI_SELECT_OPTION = "MULTI_SELECT_OPTION"
    HIDDEN_FIELDS = "HIDDEN_FIELDS"
    CALCULATED_FIELDS = "CALCULATED_FIELDS"

    def visit(
        self,
        input_text: typing.Callable[[], T_Result],
        input_number: typing.Callable[[], T_Result],
        input_email: typing.Callable[[], T_Result],
        input_link: typing.Callable[[], T_Result],
        input_phone_number: typing.Callable[[], T_Result],
        input_date: typing.Callable[[], T_Result],
        input_time: typing.Callable[[], T_Result],
        textarea: typing.Callable[[], T_Result],
        rating: typing.Callable[[], T_Result],
        linear_scale: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        multiple_choice_option: typing.Callable[[], T_Result],
        dropdown_option: typing.Callable[[], T_Result],
        ranking_option: typing.Callable[[], T_Result],
        multi_select_option: typing.Callable[[], T_Result],
        hidden_fields: typing.Callable[[], T_Result],
        calculated_fields: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldQuestionType.INPUT_TEXT:
            return input_text()
        if self is FieldQuestionType.INPUT_NUMBER:
            return input_number()
        if self is FieldQuestionType.INPUT_EMAIL:
            return input_email()
        if self is FieldQuestionType.INPUT_LINK:
            return input_link()
        if self is FieldQuestionType.INPUT_PHONE_NUMBER:
            return input_phone_number()
        if self is FieldQuestionType.INPUT_DATE:
            return input_date()
        if self is FieldQuestionType.INPUT_TIME:
            return input_time()
        if self is FieldQuestionType.TEXTAREA:
            return textarea()
        if self is FieldQuestionType.RATING:
            return rating()
        if self is FieldQuestionType.LINEAR_SCALE:
            return linear_scale()
        if self is FieldQuestionType.CHECKBOX:
            return checkbox()
        if self is FieldQuestionType.MULTIPLE_CHOICE_OPTION:
            return multiple_choice_option()
        if self is FieldQuestionType.DROPDOWN_OPTION:
            return dropdown_option()
        if self is FieldQuestionType.RANKING_OPTION:
            return ranking_option()
        if self is FieldQuestionType.MULTI_SELECT_OPTION:
            return multi_select_option()
        if self is FieldQuestionType.HIDDEN_FIELDS:
            return hidden_fields()
        if self is FieldQuestionType.CALCULATED_FIELDS:
            return calculated_fields()
