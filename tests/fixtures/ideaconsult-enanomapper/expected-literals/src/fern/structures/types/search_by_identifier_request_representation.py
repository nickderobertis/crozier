

import typing

SearchByIdentifierRequestRepresentation = typing.Union[
    typing.Literal[
        "all", "smiles", "reach", "stdinchi", "stdinchikey", "names", "iupac_name", "synonym", "cas", "einecs"
    ],
    typing.Any,
]
