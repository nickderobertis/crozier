

import typing

from .mssql_upd_perm_columns_zero import MssqlUpdPermColumnsZero

MssqlUpdPermColumns = typing.Union[MssqlUpdPermColumnsZero, typing.List[str]]
