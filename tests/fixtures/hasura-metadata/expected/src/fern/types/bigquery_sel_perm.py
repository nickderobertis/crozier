

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bigquery_bool_exp import BigqueryBoolExp
from .bigquery_sel_perm_columns import BigquerySelPermColumns
from .bigquery_sel_perm_query_root_fields_item import BigquerySelPermQueryRootFieldsItem
from .bigquery_sel_perm_subscription_root_fields_item import BigquerySelPermSubscriptionRootFieldsItem


class BigquerySelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: BigquerySelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: BigqueryBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[BigquerySelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[BigquerySelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
