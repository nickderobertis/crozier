

import typing

from .postgres_ins_perm_columns_zero import PostgresInsPermColumnsZero

PostgresInsPermColumns = typing.Union[PostgresInsPermColumnsZero, typing.List[str]]
