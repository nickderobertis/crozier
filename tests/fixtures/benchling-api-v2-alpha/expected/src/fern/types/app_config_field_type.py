

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigFieldType(enum.StrEnum):
    """
    Schema field's type, or null for Any.
    """

    DNA_SEQUENCE_LINK = "dna_sequence_link"
    AA_SEQUENCE_LINK = "aa_sequence_link"
    CUSTOM_ENTITY_LINK = "custom_entity_link"
    ENTITY_LINK = "entity_link"
    MIXTURE_LINK = "mixture_link"
    MOLECULE_LINK = "molecule_link"
    DROPDOWN = "dropdown"
    PART_LINK = "part_link"
    TRANSLATION_LINK = "translation_link"
    BLOB_LINK = "blob_link"
    TEXT = "text"
    LONG_TEXT = "long_text"
    BATCH_LINK = "batch_link"
    STORAGE_LINK = "storage_link"
    ENTRY_LINK = "entry_link"
    ASSAY_REQUEST_LINK = "assay_request_link"
    ASSAY_RESULT_LINK = "assay_result_link"
    ASSAY_RUN_LINK = "assay_run_link"
    BOOLEAN = "boolean"
    FLOAT = "float"
    INTEGER = "integer"
    DATETIME = "datetime"
    DATE = "date"
    JSON = "json"

    def visit(
        self,
        dna_sequence_link: typing.Callable[[], T_Result],
        aa_sequence_link: typing.Callable[[], T_Result],
        custom_entity_link: typing.Callable[[], T_Result],
        entity_link: typing.Callable[[], T_Result],
        mixture_link: typing.Callable[[], T_Result],
        molecule_link: typing.Callable[[], T_Result],
        dropdown: typing.Callable[[], T_Result],
        part_link: typing.Callable[[], T_Result],
        translation_link: typing.Callable[[], T_Result],
        blob_link: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        long_text: typing.Callable[[], T_Result],
        batch_link: typing.Callable[[], T_Result],
        storage_link: typing.Callable[[], T_Result],
        entry_link: typing.Callable[[], T_Result],
        assay_request_link: typing.Callable[[], T_Result],
        assay_result_link: typing.Callable[[], T_Result],
        assay_run_link: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigFieldType.DNA_SEQUENCE_LINK:
            return dna_sequence_link()
        if self is AppConfigFieldType.AA_SEQUENCE_LINK:
            return aa_sequence_link()
        if self is AppConfigFieldType.CUSTOM_ENTITY_LINK:
            return custom_entity_link()
        if self is AppConfigFieldType.ENTITY_LINK:
            return entity_link()
        if self is AppConfigFieldType.MIXTURE_LINK:
            return mixture_link()
        if self is AppConfigFieldType.MOLECULE_LINK:
            return molecule_link()
        if self is AppConfigFieldType.DROPDOWN:
            return dropdown()
        if self is AppConfigFieldType.PART_LINK:
            return part_link()
        if self is AppConfigFieldType.TRANSLATION_LINK:
            return translation_link()
        if self is AppConfigFieldType.BLOB_LINK:
            return blob_link()
        if self is AppConfigFieldType.TEXT:
            return text()
        if self is AppConfigFieldType.LONG_TEXT:
            return long_text()
        if self is AppConfigFieldType.BATCH_LINK:
            return batch_link()
        if self is AppConfigFieldType.STORAGE_LINK:
            return storage_link()
        if self is AppConfigFieldType.ENTRY_LINK:
            return entry_link()
        if self is AppConfigFieldType.ASSAY_REQUEST_LINK:
            return assay_request_link()
        if self is AppConfigFieldType.ASSAY_RESULT_LINK:
            return assay_result_link()
        if self is AppConfigFieldType.ASSAY_RUN_LINK:
            return assay_run_link()
        if self is AppConfigFieldType.BOOLEAN:
            return boolean()
        if self is AppConfigFieldType.FLOAT:
            return float_()
        if self is AppConfigFieldType.INTEGER:
            return integer()
        if self is AppConfigFieldType.DATETIME:
            return datetime()
        if self is AppConfigFieldType.DATE:
            return date()
        if self is AppConfigFieldType.JSON:
            return json()
