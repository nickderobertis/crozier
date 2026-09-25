

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BlockType(enum.StrEnum):
    FORM_TITLE = "FORM_TITLE"
    TEXT = "TEXT"
    LABEL = "LABEL"
    TITLE = "TITLE"
    HEADING1 = "HEADING_1"
    HEADING2 = "HEADING_2"
    HEADING3 = "HEADING_3"
    DIVIDER = "DIVIDER"
    PAGE_BREAK = "PAGE_BREAK"
    IMAGE = "IMAGE"
    EMBED = "EMBED"
    EMBED_VIDEO = "EMBED_VIDEO"
    EMBED_AUDIO = "EMBED_AUDIO"
    QUESTION = "QUESTION"
    MATRIX = "MATRIX"
    INPUT_TEXT = "INPUT_TEXT"
    INPUT_NUMBER = "INPUT_NUMBER"
    INPUT_EMAIL = "INPUT_EMAIL"
    INPUT_LINK = "INPUT_LINK"
    INPUT_PHONE_NUMBER = "INPUT_PHONE_NUMBER"
    INPUT_DATE = "INPUT_DATE"
    INPUT_TIME = "INPUT_TIME"
    TEXTAREA = "TEXTAREA"
    FILE_UPLOAD = "FILE_UPLOAD"
    LINEAR_SCALE = "LINEAR_SCALE"
    RATING = "RATING"
    HIDDEN_FIELDS = "HIDDEN_FIELDS"
    MULTIPLE_CHOICE_OPTION = "MULTIPLE_CHOICE_OPTION"
    CHECKBOX = "CHECKBOX"
    DROPDOWN_OPTION = "DROPDOWN_OPTION"
    RANKING_OPTION = "RANKING_OPTION"
    MULTI_SELECT_OPTION = "MULTI_SELECT_OPTION"
    PAYMENT = "PAYMENT"
    SIGNATURE = "SIGNATURE"
    MATRIX_ROW = "MATRIX_ROW"
    MATRIX_COLUMN = "MATRIX_COLUMN"
    WALLET_CONNECT = "WALLET_CONNECT"
    CONDITIONAL_LOGIC = "CONDITIONAL_LOGIC"
    CALCULATED_FIELDS = "CALCULATED_FIELDS"
    CAPTCHA = "CAPTCHA"
    RESPONDENT_COUNTRY = "RESPONDENT_COUNTRY"

    def visit(
        self,
        form_title: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        label: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        heading1: typing.Callable[[], T_Result],
        heading2: typing.Callable[[], T_Result],
        heading3: typing.Callable[[], T_Result],
        divider: typing.Callable[[], T_Result],
        page_break: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        embed: typing.Callable[[], T_Result],
        embed_video: typing.Callable[[], T_Result],
        embed_audio: typing.Callable[[], T_Result],
        question: typing.Callable[[], T_Result],
        matrix: typing.Callable[[], T_Result],
        input_text: typing.Callable[[], T_Result],
        input_number: typing.Callable[[], T_Result],
        input_email: typing.Callable[[], T_Result],
        input_link: typing.Callable[[], T_Result],
        input_phone_number: typing.Callable[[], T_Result],
        input_date: typing.Callable[[], T_Result],
        input_time: typing.Callable[[], T_Result],
        textarea: typing.Callable[[], T_Result],
        file_upload: typing.Callable[[], T_Result],
        linear_scale: typing.Callable[[], T_Result],
        rating: typing.Callable[[], T_Result],
        hidden_fields: typing.Callable[[], T_Result],
        multiple_choice_option: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        dropdown_option: typing.Callable[[], T_Result],
        ranking_option: typing.Callable[[], T_Result],
        multi_select_option: typing.Callable[[], T_Result],
        payment: typing.Callable[[], T_Result],
        signature: typing.Callable[[], T_Result],
        matrix_row: typing.Callable[[], T_Result],
        matrix_column: typing.Callable[[], T_Result],
        wallet_connect: typing.Callable[[], T_Result],
        conditional_logic: typing.Callable[[], T_Result],
        calculated_fields: typing.Callable[[], T_Result],
        captcha: typing.Callable[[], T_Result],
        respondent_country: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BlockType.FORM_TITLE:
            return form_title()
        if self is BlockType.TEXT:
            return text()
        if self is BlockType.LABEL:
            return label()
        if self is BlockType.TITLE:
            return title()
        if self is BlockType.HEADING1:
            return heading1()
        if self is BlockType.HEADING2:
            return heading2()
        if self is BlockType.HEADING3:
            return heading3()
        if self is BlockType.DIVIDER:
            return divider()
        if self is BlockType.PAGE_BREAK:
            return page_break()
        if self is BlockType.IMAGE:
            return image()
        if self is BlockType.EMBED:
            return embed()
        if self is BlockType.EMBED_VIDEO:
            return embed_video()
        if self is BlockType.EMBED_AUDIO:
            return embed_audio()
        if self is BlockType.QUESTION:
            return question()
        if self is BlockType.MATRIX:
            return matrix()
        if self is BlockType.INPUT_TEXT:
            return input_text()
        if self is BlockType.INPUT_NUMBER:
            return input_number()
        if self is BlockType.INPUT_EMAIL:
            return input_email()
        if self is BlockType.INPUT_LINK:
            return input_link()
        if self is BlockType.INPUT_PHONE_NUMBER:
            return input_phone_number()
        if self is BlockType.INPUT_DATE:
            return input_date()
        if self is BlockType.INPUT_TIME:
            return input_time()
        if self is BlockType.TEXTAREA:
            return textarea()
        if self is BlockType.FILE_UPLOAD:
            return file_upload()
        if self is BlockType.LINEAR_SCALE:
            return linear_scale()
        if self is BlockType.RATING:
            return rating()
        if self is BlockType.HIDDEN_FIELDS:
            return hidden_fields()
        if self is BlockType.MULTIPLE_CHOICE_OPTION:
            return multiple_choice_option()
        if self is BlockType.CHECKBOX:
            return checkbox()
        if self is BlockType.DROPDOWN_OPTION:
            return dropdown_option()
        if self is BlockType.RANKING_OPTION:
            return ranking_option()
        if self is BlockType.MULTI_SELECT_OPTION:
            return multi_select_option()
        if self is BlockType.PAYMENT:
            return payment()
        if self is BlockType.SIGNATURE:
            return signature()
        if self is BlockType.MATRIX_ROW:
            return matrix_row()
        if self is BlockType.MATRIX_COLUMN:
            return matrix_column()
        if self is BlockType.WALLET_CONNECT:
            return wallet_connect()
        if self is BlockType.CONDITIONAL_LOGIC:
            return conditional_logic()
        if self is BlockType.CALCULATED_FIELDS:
            return calculated_fields()
        if self is BlockType.CAPTCHA:
            return captcha()
        if self is BlockType.RESPONDENT_COUNTRY:
            return respondent_country()
