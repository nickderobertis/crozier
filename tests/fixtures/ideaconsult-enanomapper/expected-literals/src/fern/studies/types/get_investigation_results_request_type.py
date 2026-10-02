

import typing

GetInvestigationResultsRequestType = typing.Union[
    typing.Literal[
        "byinvestigation",
        "byassay",
        "bysubstance",
        "byprovider",
        "bycitation",
        "bystudytype",
        "bystructure_inchikey",
        "bystructure_smiles",
        "bystructure_name",
        "bysubstance_name",
        "bysubstance_type",
    ],
    typing.Any,
]
