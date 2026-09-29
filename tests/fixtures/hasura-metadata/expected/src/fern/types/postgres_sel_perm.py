

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_bool_exp import PostgresBoolExp
from .postgres_sel_perm_columns import PostgresSelPermColumns
from .postgres_sel_perm_query_root_fields_item import PostgresSelPermQueryRootFieldsItem
from .postgres_sel_perm_subscription_root_fields_item import PostgresSelPermSubscriptionRootFieldsItem


class PostgresSelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: PostgresSelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: PostgresBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[PostgresSelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[PostgresSelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
