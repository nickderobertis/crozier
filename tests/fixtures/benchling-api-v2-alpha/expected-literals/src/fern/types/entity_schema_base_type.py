

import typing

EntitySchemaBaseType = typing.Union[
    typing.Literal[
        "custom_entity",
        "dna_sequence",
        "rna_sequence",
        "aa_sequence",
        "mixture",
        "dna_oligo",
        "rna_oligo",
        "molecule",
        "entry",
    ],
    typing.Any,
]
