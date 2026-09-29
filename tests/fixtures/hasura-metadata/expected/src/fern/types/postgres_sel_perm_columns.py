

import typing

from .postgres_sel_perm_columns_zero import PostgresSelPermColumnsZero

PostgresSelPermColumns = typing.Union[PostgresSelPermColumnsZero, typing.List[str]]
