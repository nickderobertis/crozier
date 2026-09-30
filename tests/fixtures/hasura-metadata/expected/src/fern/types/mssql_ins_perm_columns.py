

import typing

from .mssql_ins_perm_columns_zero import MssqlInsPermColumnsZero

MssqlInsPermColumns = typing.Union[MssqlInsPermColumnsZero, typing.List[str]]
