

import typing

from .mssql_sel_perm_columns_zero import MssqlSelPermColumnsZero

MssqlSelPermColumns = typing.Union[MssqlSelPermColumnsZero, typing.List[str]]
