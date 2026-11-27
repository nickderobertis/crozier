

import typing

ResourceDependencyTypes = typing.Union[
    typing.Literal[
        "aa_sequence",
        "box",
        "container",
        "custom_entity",
        "dna_oligo",
        "dna_sequence",
        "entry",
        "folder",
        "location",
        "mixture",
        "molecule",
        "plate",
        "project",
        "registry",
        "rna_oligo",
        "rna_sequence",
        "workflow_task_status",
        "worklist",
    ],
    typing.Any,
]
