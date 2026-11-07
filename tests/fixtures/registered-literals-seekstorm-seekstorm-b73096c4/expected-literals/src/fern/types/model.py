

import typing

Model = typing.Union[
    typing.Literal[
        "PotionCode16MV2",
        "PotionBase32M",
        "PotionMultilingual128M",
        "PotionRetrieval32M",
        "PotionBase8M",
        "PotionBase4M",
        "PotionBase2M",
    ],
    typing.Any,
]
