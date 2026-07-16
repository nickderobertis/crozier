

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_bulk_data_exporter_configs_response_item_status import CreateBulkDataExporterConfigsResponseItemStatus


class CreateBulkDataExporterConfigsResponseItem(UniversalBaseModel):
    """
    The bulk response
    """

    created: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the action was carried out correctly or not
    """

    id: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Data exporter id
    """

    status: typing.Optional[CreateBulkDataExporterConfigsResponseItemStatus] = pydantic.Field(default=None)
    """
    Status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
