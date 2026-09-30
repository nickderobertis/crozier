

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .big_query_conn_source_config_datasets import BigQueryConnSourceConfigDatasets
from .big_query_conn_source_config_global_select_limit import BigQueryConnSourceConfigGlobalSelectLimit
from .big_query_conn_source_config_project_id import BigQueryConnSourceConfigProjectId
from .big_query_conn_source_config_retry_base_delay import BigQueryConnSourceConfigRetryBaseDelay
from .big_query_conn_source_config_retry_limit import BigQueryConnSourceConfigRetryLimit


class BigQueryConnSourceConfig(UniversalBaseModel):
    datasets: BigQueryConnSourceConfigDatasets
    global_select_limit: typing.Optional[BigQueryConnSourceConfigGlobalSelectLimit] = None
    project_id: BigQueryConnSourceConfigProjectId
    retry_base_delay: typing.Optional[BigQueryConnSourceConfigRetryBaseDelay] = None
    retry_limit: typing.Optional[BigQueryConnSourceConfigRetryLimit] = None
    service_account: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
