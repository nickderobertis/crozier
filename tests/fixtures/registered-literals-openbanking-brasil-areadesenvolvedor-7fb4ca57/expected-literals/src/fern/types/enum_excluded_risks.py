

import typing

EnumExcludedRisks = typing.Union[
    typing.Literal[
        "ATO_RECONHECIMENTO_PERIGOSO",
        "ATO_ILICITO_DOLOSO_PRATICADO_SEGURADO",
        "OPERACOES_GUERRA",
        "FURACOES_CICLONES_TERREMOTOS",
        "MATERIAL_NUCLEAR",
        "DOENCAS_LESOES_PREEXISTENTES",
        "EPIDEMIAS_PANDEMIAS",
        "SUICIDIO",
        "ATO_ILICITO_DOLOSO_PRATICADO_CONTROLADOR",
        "OUTROS",
    ],
    typing.Any,
]
