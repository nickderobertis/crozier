

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldType(enum.StrEnum):
    DNA_SEQUENCE_LINK = "dna_sequence_link"
    AA_SEQUENCE_LINK = "aa_sequence_link"
    CUSTOM_ENTITY_LINK = "custom_entity_link"
    ENTITY_LINK = "entity_link"
    MIXTURE_LINK = "mixture_link"
    MOLECULE_LINK = "molecule_link"
    DROPDOWN = "dropdown"
    PART_LINK = "part_link"
    TRANSLATION_LINK = "translation_link"
    AA_PART_LINK = "aa_part_link"
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
        aa_part_link: typing.Callable[[], T_Result],
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
        if self is FieldType.DNA_SEQUENCE_LINK:
            return dna_sequence_link()
        if self is FieldType.AA_SEQUENCE_LINK:
            return aa_sequence_link()
        if self is FieldType.CUSTOM_ENTITY_LINK:
            return custom_entity_link()
        if self is FieldType.ENTITY_LINK:
            return entity_link()
        if self is FieldType.MIXTURE_LINK:
            return mixture_link()
        if self is FieldType.MOLECULE_LINK:
            return molecule_link()
        if self is FieldType.DROPDOWN:
            return dropdown()
        if self is FieldType.PART_LINK:
            return part_link()
        if self is FieldType.TRANSLATION_LINK:
            return translation_link()
        if self is FieldType.AA_PART_LINK:
            return aa_part_link()
        if self is FieldType.BLOB_LINK:
            return blob_link()
        if self is FieldType.TEXT:
            return text()
        if self is FieldType.LONG_TEXT:
            return long_text()
        if self is FieldType.BATCH_LINK:
            return batch_link()
        if self is FieldType.STORAGE_LINK:
            return storage_link()
        if self is FieldType.ENTRY_LINK:
            return entry_link()
        if self is FieldType.ASSAY_REQUEST_LINK:
            return assay_request_link()
        if self is FieldType.ASSAY_RESULT_LINK:
            return assay_result_link()
        if self is FieldType.ASSAY_RUN_LINK:
            return assay_run_link()
        if self is FieldType.BOOLEAN:
            return boolean()
        if self is FieldType.FLOAT:
            return float_()
        if self is FieldType.INTEGER:
            return integer()
        if self is FieldType.DATETIME:
            return datetime()
        if self is FieldType.DATE:
            return date()
        if self is FieldType.JSON:
            return json()
