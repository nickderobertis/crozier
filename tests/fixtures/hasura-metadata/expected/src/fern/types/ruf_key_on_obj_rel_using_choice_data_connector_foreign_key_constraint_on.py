

import typing

from .dataconnector_obj_rel_remote_table_multiple_columns import DataconnectorObjRelRemoteTableMultipleColumns
from .dataconnector_obj_rel_remote_table_single_column import DataconnectorObjRelRemoteTableSingleColumn
from .ruf_key_on_obj_rel_using_choice_data_connector_foreign_key_constraint_on_two_item import (
    RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOnTwoItem,
)

RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOn = typing.Union[
    typing.List[str],
    str,
    typing.List[RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOnTwoItem],
    DataconnectorObjRelRemoteTableSingleColumn,
    DataconnectorObjRelRemoteTableMultipleColumns,
]
