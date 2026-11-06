

import typing

BadgeType = typing.Union[
    typing.Literal[
        "next_level",
        "next_level_class",
        "report",
        "new_report",
        "two_shops",
        "shop_first_report",
        "week_1",
        "week_3",
        "week_full",
        "week_special",
        "trusted_shop",
        "trusted_user",
    ],
    typing.Any,
]
