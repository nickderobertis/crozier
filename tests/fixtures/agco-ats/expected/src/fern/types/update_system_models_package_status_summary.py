

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_package_status import UpdateSystemModelsPackageStatus


class UpdateSystemModelsPackageStatusSummary(UniversalBaseModel):
    average_download_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AverageDownloadTime"),
        pydantic.Field(alias="AverageDownloadTime", description="The average time required to complete the download"),
    ] = None
    """
    The average time required to complete the download
    """

    average_install_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AverageInstallTime"),
        pydantic.Field(alias="AverageInstallTime", description="The average time required to complete the install"),
    ] = None
    """
    The average time required to complete the install
    """

    downloaded: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Downloaded"),
        pydantic.Field(alias="Downloaded", description="The number of clients that have completed the download"),
    ] = None
    """
    The number of clients that have completed the download
    """

    error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Error"),
        pydantic.Field(alias="Error", description="The result of the install"),
    ] = None
    """
    The result of the install
    """

    installed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Installed"),
        pydantic.Field(alias="Installed", description="The number of clients that have completed the install"),
    ] = None
    """
    The number of clients that have completed the install
    """

    package: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Package"),
        pydantic.Field(alias="Package", description="The name of the package"),
    ] = None
    """
    The name of the package
    """

    package_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageID"),
        pydantic.Field(alias="PackageID", description="The ID of the package"),
    ] = None
    """
    The ID of the package
    """

    package_status_items: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsPackageStatus]],
        FieldMetadata(alias="PackageStatusItems"),
        pydantic.Field(alias="PackageStatusItems", description="The individual package status items"),
    ] = None
    """
    The individual package status items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
