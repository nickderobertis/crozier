

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_bulk_data_exporter_config_response_item_status import UpdateBulkDataExporterConfigResponseItemStatus


class UpdateBulkDataExporterConfigResponseItem(UniversalBaseModel):
    """
    The bulk response
    """

    id: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Data exporter id
    """

    status: typing.Optional[UpdateBulkDataExporterConfigResponseItemStatus] = pydantic.Field(default=None)
    """
    Status
    """

    updated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the action was carried out correctly or not
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
