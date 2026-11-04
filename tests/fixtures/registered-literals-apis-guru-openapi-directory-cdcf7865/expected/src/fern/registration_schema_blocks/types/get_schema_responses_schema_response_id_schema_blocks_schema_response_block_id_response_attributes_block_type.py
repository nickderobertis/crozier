

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType(enum.StrEnum):
    """
    A string that represents the type of input that the schema will take and the UI element that appears to the user on the frontend.
    """

    PAGE_HEADING = "page-heading"
    SECTION_HEADING = "section-heading"
    SUBSECTION_HEADING = "subsection-heading"
    PARAGRAPH = "paragraph"
    QUESTION_LABEL = "question-label"
    SHORT_TEXT_INPUT = "short-text-input"
    LONG_TEXT_INPUT = "long-text-input"
    FILE_INPUT = "file-input"
    CONTRIBUTORS_INPUT = "contributors-input"
    SINGLE_SELECT_INPUT = "single-select-input"
    MULTI_SELECT_INPUT = "multi-select-input"
    SELECT_INPUT_OPTION = "select-input-option"
    SELECT_OTHER_OPTION = "select-other-option"

    def visit(
        self,
        page_heading: typing.Callable[[], T_Result],
        section_heading: typing.Callable[[], T_Result],
        subsection_heading: typing.Callable[[], T_Result],
        paragraph: typing.Callable[[], T_Result],
        question_label: typing.Callable[[], T_Result],
        short_text_input: typing.Callable[[], T_Result],
        long_text_input: typing.Callable[[], T_Result],
        file_input: typing.Callable[[], T_Result],
        contributors_input: typing.Callable[[], T_Result],
        single_select_input: typing.Callable[[], T_Result],
        multi_select_input: typing.Callable[[], T_Result],
        select_input_option: typing.Callable[[], T_Result],
        select_other_option: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.PAGE_HEADING
        ):
            return page_heading()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SECTION_HEADING
        ):
            return section_heading()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SUBSECTION_HEADING
        ):
            return subsection_heading()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.PARAGRAPH
        ):
            return paragraph()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.QUESTION_LABEL
        ):
            return question_label()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SHORT_TEXT_INPUT
        ):
            return short_text_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.LONG_TEXT_INPUT
        ):
            return long_text_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.FILE_INPUT
        ):
            return file_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.CONTRIBUTORS_INPUT
        ):
            return contributors_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SINGLE_SELECT_INPUT
        ):
            return single_select_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.MULTI_SELECT_INPUT
        ):
            return multi_select_input()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SELECT_INPUT_OPTION
        ):
            return select_input_option()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType.SELECT_OTHER_OPTION
        ):
            return select_other_option()
