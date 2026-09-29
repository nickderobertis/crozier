

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_bool_exp import DataconnectorBoolExp
from .dataconnector_sel_perm_columns import DataconnectorSelPermColumns
from .dataconnector_sel_perm_query_root_fields_item import DataconnectorSelPermQueryRootFieldsItem
from .dataconnector_sel_perm_subscription_root_fields_item import DataconnectorSelPermSubscriptionRootFieldsItem


class DataconnectorSelPerm(UniversalBaseModel):
    allow_aggregations: typing.Optional[bool] = None
    columns: DataconnectorSelPermColumns
    computed_fields: typing.Optional[typing.List[str]] = None
    filter: DataconnectorBoolExp
    limit: typing.Optional[float] = None
    query_root_fields: typing.Optional[typing.List[DataconnectorSelPermQueryRootFieldsItem]] = None
    subscription_root_fields: typing.Optional[typing.List[DataconnectorSelPermSubscriptionRootFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
