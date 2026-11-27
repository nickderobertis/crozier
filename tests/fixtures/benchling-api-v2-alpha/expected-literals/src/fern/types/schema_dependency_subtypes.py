

import typing

SchemaDependencySubtypes = typing.Union[
    typing.Literal[
        "aa_sequence", "dna_sequence", "custom_entity", "mixture", "molecule", "dna_oligo", "rna_oligo", "rna_sequence"
    ],
    typing.Any,
]
