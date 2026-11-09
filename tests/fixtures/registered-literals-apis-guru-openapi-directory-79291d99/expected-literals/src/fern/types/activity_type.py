

import typing

ActivityType = typing.Union[
    typing.Literal[
        "UNKNOWN",
        "ITEM_CREATE",
        "ITEM_IMPORT",
        "ITEM_UPDATE",
        "ITEM_UNLINK",
        "PORTAL_UNLINK",
        "PORTAL_ITEMS_DELETE",
        "ITEM_REMOVE",
        "INVARIANT_CHECKER_DELETION",
        "SCOPES_UPDATE",
    ],
    typing.Any,
]
