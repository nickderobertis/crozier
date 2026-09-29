

import typing

from .cockroach_upd_perm_columns_zero import CockroachUpdPermColumnsZero

CockroachUpdPermColumns = typing.Union[CockroachUpdPermColumnsZero, typing.List[str]]
