

import typing

from .mssql_obj_rel_remote_table_multiple_columns import MssqlObjRelRemoteTableMultipleColumns
from .mssql_obj_rel_remote_table_single_column import MssqlObjRelRemoteTableSingleColumn

RufKeyOnObjRelUsingChoiceMssqlForeignKeyConstraintOn = typing.Union[
    str, typing.List[str], MssqlObjRelRemoteTableSingleColumn, MssqlObjRelRemoteTableMultipleColumns
]
