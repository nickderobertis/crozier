

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_bool_exp import MssqlBoolExp
from .mssql_sel_perm_columns import MssqlSelPermColumns
from .mssql_sel_perm_query_root_fields_item import MssqlSelPermQueryRootFieldsItem
from .mssql_sel_perm_subscription_root_fields_item import MssqlSelPermSubscriptionRootFieldsItem


class MssqlSelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: MssqlSelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: MssqlBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[MssqlSelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[MssqlSelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
