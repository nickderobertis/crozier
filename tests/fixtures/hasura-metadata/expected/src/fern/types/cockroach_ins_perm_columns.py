

import typing

from .cockroach_ins_perm_columns_zero import CockroachInsPermColumnsZero

CockroachInsPermColumns = typing.Union[CockroachInsPermColumnsZero, typing.List[str]]
