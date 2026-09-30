

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .table_custom_root_fields_delete import TableCustomRootFieldsDelete
from .table_custom_root_fields_delete_by_pk import TableCustomRootFieldsDeleteByPk
from .table_custom_root_fields_insert import TableCustomRootFieldsInsert
from .table_custom_root_fields_insert_one import TableCustomRootFieldsInsertOne
from .table_custom_root_fields_select import TableCustomRootFieldsSelect
from .table_custom_root_fields_select_aggregate import TableCustomRootFieldsSelectAggregate
from .table_custom_root_fields_select_by_pk import TableCustomRootFieldsSelectByPk
from .table_custom_root_fields_select_stream import TableCustomRootFieldsSelectStream
from .table_custom_root_fields_update import TableCustomRootFieldsUpdate
from .table_custom_root_fields_update_by_pk import TableCustomRootFieldsUpdateByPk
from .table_custom_root_fields_update_many import TableCustomRootFieldsUpdateMany


class TableCustomRootFields(UniversalBaseModel):
    delete: typing.Optional[TableCustomRootFieldsDelete] = None
    delete_by_pk: typing.Optional[TableCustomRootFieldsDeleteByPk] = None
    insert: typing.Optional[TableCustomRootFieldsInsert] = None
    insert_one: typing.Optional[TableCustomRootFieldsInsertOne] = None
    select: typing.Optional[TableCustomRootFieldsSelect] = None
    select_aggregate: typing.Optional[TableCustomRootFieldsSelectAggregate] = None
    select_by_pk: typing.Optional[TableCustomRootFieldsSelectByPk] = None
    select_stream: typing.Optional[TableCustomRootFieldsSelectStream] = None
    update: typing.Optional[TableCustomRootFieldsUpdate] = None
    update_by_pk: typing.Optional[TableCustomRootFieldsUpdateByPk] = None
    update_many: typing.Optional[TableCustomRootFieldsUpdateMany] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
