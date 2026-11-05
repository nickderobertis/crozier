

import typing

PublicationHistoryItemMethod = typing.Union[
    typing.Literal["manual", "automatic_after_approval", "scheduled", "rollback", "migration", "backfill"], typing.Any
]
