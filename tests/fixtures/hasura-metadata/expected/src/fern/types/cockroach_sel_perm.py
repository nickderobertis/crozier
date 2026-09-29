

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cockroach_bool_exp import CockroachBoolExp
from .cockroach_sel_perm_columns import CockroachSelPermColumns
from .cockroach_sel_perm_query_root_fields_item import CockroachSelPermQueryRootFieldsItem
from .cockroach_sel_perm_subscription_root_fields_item import CockroachSelPermSubscriptionRootFieldsItem


class CockroachSelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: CockroachSelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: CockroachBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[CockroachSelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[CockroachSelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
