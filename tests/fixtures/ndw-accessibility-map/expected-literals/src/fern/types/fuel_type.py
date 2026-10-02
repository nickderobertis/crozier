

import typing

FuelType = typing.Union[
    typing.Literal[
        "electric",
        "diesel",
        "hydrogen",
        "liquefied_petroleum_gas",
        "compressed_natural_gas",
        "liquefied_natural_gas",
        "ethanol",
        "petrol",
    ],
    typing.Any,
]
