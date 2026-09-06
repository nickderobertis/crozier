

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FormSubmissionPayloadPayloadSchemaItemFieldType(enum.StrEnum):
    """
    Form field type
    """

    FORM_TEXT_INPUT = "FormTextInput"
    FORM_TEXTAREA = "FormTextarea"
    FORM_CHECKBOX_INPUT = "FormCheckboxInput"
    FORM_RADIO_INPUT = "FormRadioInput"
    FORM_FILE_UPLOAD_INPUT = "FormFileUploadInput"

    def visit(
        self,
        form_text_input: typing.Callable[[], T_Result],
        form_textarea: typing.Callable[[], T_Result],
        form_checkbox_input: typing.Callable[[], T_Result],
        form_radio_input: typing.Callable[[], T_Result],
        form_file_upload_input: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FormSubmissionPayloadPayloadSchemaItemFieldType.FORM_TEXT_INPUT:
            return form_text_input()
        if self is FormSubmissionPayloadPayloadSchemaItemFieldType.FORM_TEXTAREA:
            return form_textarea()
        if self is FormSubmissionPayloadPayloadSchemaItemFieldType.FORM_CHECKBOX_INPUT:
            return form_checkbox_input()
        if self is FormSubmissionPayloadPayloadSchemaItemFieldType.FORM_RADIO_INPUT:
            return form_radio_input()
        if self is FormSubmissionPayloadPayloadSchemaItemFieldType.FORM_FILE_UPLOAD_INPUT:
            return form_file_upload_input()
