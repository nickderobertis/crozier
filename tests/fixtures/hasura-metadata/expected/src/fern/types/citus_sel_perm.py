

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citus_bool_exp import CitusBoolExp
from .citus_sel_perm_columns import CitusSelPermColumns
from .citus_sel_perm_query_root_fields_item import CitusSelPermQueryRootFieldsItem
from .citus_sel_perm_subscription_root_fields_item import CitusSelPermSubscriptionRootFieldsItem


class CitusSelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: CitusSelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: CitusBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[CitusSelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[CitusSelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
