

import typing

from .cockroach_sel_perm_columns_zero import CockroachSelPermColumnsZero

CockroachSelPermColumns = typing.Union[CockroachSelPermColumnsZero, typing.List[str]]
