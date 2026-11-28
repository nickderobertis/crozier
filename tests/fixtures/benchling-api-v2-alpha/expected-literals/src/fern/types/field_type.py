

import typing

FieldType = typing.Union[
    typing.Literal[
        "dna_sequence_link",
        "aa_sequence_link",
        "custom_entity_link",
        "entity_link",
        "mixture_link",
        "molecule_link",
        "dropdown",
        "part_link",
        "translation_link",
        "aa_part_link",
        "blob_link",
        "text",
        "long_text",
        "batch_link",
        "storage_link",
        "entry_link",
        "assay_request_link",
        "assay_result_link",
        "assay_run_link",
        "boolean",
        "float",
        "integer",
        "datetime",
        "date",
        "json",
    ],
    typing.Any,
]
