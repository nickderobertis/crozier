

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_update_metrics_data_active_version_by_client_record import (
    UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord,
)
from .update_system_models_update_metrics_data_current_state_by_client_record import (
    UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord,
)
from .update_system_models_update_metrics_data_package_errors_record import (
    UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord,
)


class UpdateSystemModelsUpdateMetricsData(UniversalBaseModel):
    """
    Model that retrieves the data for UpdateMetrics
    """

    active_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ActiveVersion"),
        pydantic.Field(alias="ActiveVersion", description="Active version (bundle number) of update type."),
    ] = None
    """
    Active version (bundle number) of update type.
    """

    active_version_by_client: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord]],
        FieldMetadata(alias="ActiveVersionByClient"),
        pydantic.Field(
            alias="ActiveVersionByClient", description="Generic collection that is of type ActiveVersionByClientRecord"
        ),
    ] = None
    """
    Generic collection that is of type ActiveVersionByClientRecord
    """

    current_state_by_client: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord]],
        FieldMetadata(alias="CurrentStateByClient"),
        pydantic.Field(
            alias="CurrentStateByClient", description="Generic collection that is of type CurrentStateByClientRecord"
        ),
    ] = None
    """
    Generic collection that is of type CurrentStateByClientRecord
    """

    cut_off_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CutOffDate"),
        pydantic.Field(
            alias="CutOffDate",
            description="Date that has been configured to only show the most recent clients with a cut off date. (Ex. year from current date)",
        ),
    ] = None
    """
    Date that has been configured to only show the most recent clients with a cut off date. (Ex. year from current date)
    """

    data_refreshed: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="DataRefreshed"),
        pydantic.Field(alias="DataRefreshed", description="Data was refreshed at this time."),
    ] = None
    """
    Data was refreshed at this time.
    """

    filtered_client_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="FilteredClientCount"),
        pydantic.Field(
            alias="FilteredClientCount",
            description="Sum of clients represented\r\n            Filtered by updateType and lastCheckedInDate",
        ),
    ] = None
    """
    Sum of clients represented
                Filtered by updateType and lastCheckedInDate
    """

    package_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord]],
        FieldMetadata(alias="PackageErrors"),
        pydantic.Field(alias="PackageErrors", description="Generic collection that is of type PackageErrorsRecord"),
    ] = None
    """
    Generic collection that is of type PackageErrorsRecord
    """

    total_client_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TotalClientCount"),
        pydantic.Field(alias="TotalClientCount", description="Total clients we have ever serviced"),
    ] = None
    """
    Total clients we have ever serviced
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
