

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BlockType(enum.StrEnum):
    TASK = "task"
    TASK_V2 = "task_v2"
    FOR_LOOP = "for_loop"
    WHILE_LOOP = "while_loop"
    CONDITIONAL = "conditional"
    CODE = "code"
    TEXT_PROMPT = "text_prompt"
    DOWNLOAD_TO_S3 = "download_to_s3"
    UPLOAD_TO_S3 = "upload_to_s3"
    FILE_UPLOAD = "file_upload"
    SEND_EMAIL = "send_email"
    FILE_URL_PARSER = "file_url_parser"
    VALIDATION = "validation"
    ACTION = "action"
    NAVIGATION = "navigation"
    EXTRACTION = "extraction"
    LOGIN = "login"
    WAIT = "wait"
    FILE_DOWNLOAD = "file_download"
    GOTO_URL = "goto_url"
    PDF_PARSER = "pdf_parser"
    HTTP_REQUEST = "http_request"
    HUMAN_INTERACTION = "human_interaction"
    PRINT_PAGE = "print_page"
    WORKFLOW_TRIGGER = "workflow_trigger"
    GOOGLE_SHEETS_READ = "google_sheets_read"
    GOOGLE_SHEETS_WRITE = "google_sheets_write"
    PDF_FILL = "pdf_fill"
    SPLIT_PDF = "split_pdf"
    EMAIL_INBOX = "email_inbox"

    def visit(
        self,
        task: typing.Callable[[], T_Result],
        task_v2: typing.Callable[[], T_Result],
        for_loop: typing.Callable[[], T_Result],
        while_loop: typing.Callable[[], T_Result],
        conditional: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        text_prompt: typing.Callable[[], T_Result],
        download_to_s3: typing.Callable[[], T_Result],
        upload_to_s3: typing.Callable[[], T_Result],
        file_upload: typing.Callable[[], T_Result],
        send_email: typing.Callable[[], T_Result],
        file_url_parser: typing.Callable[[], T_Result],
        validation: typing.Callable[[], T_Result],
        action: typing.Callable[[], T_Result],
        navigation: typing.Callable[[], T_Result],
        extraction: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
        wait: typing.Callable[[], T_Result],
        file_download: typing.Callable[[], T_Result],
        goto_url: typing.Callable[[], T_Result],
        pdf_parser: typing.Callable[[], T_Result],
        http_request: typing.Callable[[], T_Result],
        human_interaction: typing.Callable[[], T_Result],
        print_page: typing.Callable[[], T_Result],
        workflow_trigger: typing.Callable[[], T_Result],
        google_sheets_read: typing.Callable[[], T_Result],
        google_sheets_write: typing.Callable[[], T_Result],
        pdf_fill: typing.Callable[[], T_Result],
        split_pdf: typing.Callable[[], T_Result],
        email_inbox: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BlockType.TASK:
            return task()
        if self is BlockType.TASK_V2:
            return task_v2()
        if self is BlockType.FOR_LOOP:
            return for_loop()
        if self is BlockType.WHILE_LOOP:
            return while_loop()
        if self is BlockType.CONDITIONAL:
            return conditional()
        if self is BlockType.CODE:
            return code()
        if self is BlockType.TEXT_PROMPT:
            return text_prompt()
        if self is BlockType.DOWNLOAD_TO_S3:
            return download_to_s3()
        if self is BlockType.UPLOAD_TO_S3:
            return upload_to_s3()
        if self is BlockType.FILE_UPLOAD:
            return file_upload()
        if self is BlockType.SEND_EMAIL:
            return send_email()
        if self is BlockType.FILE_URL_PARSER:
            return file_url_parser()
        if self is BlockType.VALIDATION:
            return validation()
        if self is BlockType.ACTION:
            return action()
        if self is BlockType.NAVIGATION:
            return navigation()
        if self is BlockType.EXTRACTION:
            return extraction()
        if self is BlockType.LOGIN:
            return login()
        if self is BlockType.WAIT:
            return wait()
        if self is BlockType.FILE_DOWNLOAD:
            return file_download()
        if self is BlockType.GOTO_URL:
            return goto_url()
        if self is BlockType.PDF_PARSER:
            return pdf_parser()
        if self is BlockType.HTTP_REQUEST:
            return http_request()
        if self is BlockType.HUMAN_INTERACTION:
            return human_interaction()
        if self is BlockType.PRINT_PAGE:
            return print_page()
        if self is BlockType.WORKFLOW_TRIGGER:
            return workflow_trigger()
        if self is BlockType.GOOGLE_SHEETS_READ:
            return google_sheets_read()
        if self is BlockType.GOOGLE_SHEETS_WRITE:
            return google_sheets_write()
        if self is BlockType.PDF_FILL:
            return pdf_fill()
        if self is BlockType.SPLIT_PDF:
            return split_pdf()
        if self is BlockType.EMAIL_INBOX:
            return email_inbox()
