

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsPackageStatus(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="The id of the client"),
    ] = None
    """
    The id of the client
    """

    client_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientKey"),
        pydantic.Field(alias="ClientKey", description="The client's tag"),
    ] = None
    """
    The client's tag
    """

    download_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DownloadTime"),
        pydantic.Field(alias="DownloadTime", description="The amount of time spent downloading"),
    ] = None
    """
    The amount of time spent downloading
    """

    downloaded: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Downloaded"),
        pydantic.Field(alias="Downloaded", description="The number of bytes downloaded"),
    ] = None
    """
    The number of bytes downloaded
    """

    install_completed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InstallCompleted"),
        pydantic.Field(alias="InstallCompleted", description="The time the package completed"),
    ] = None
    """
    The time the package completed
    """

    install_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InstallResult"),
        pydantic.Field(alias="InstallResult", description="The package result"),
    ] = None
    """
    The package result
    """

    install_started: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InstallStarted"),
        pydantic.Field(alias="InstallStarted", description="The time the package was started"),
    ] = None
    """
    The time the package was started
    """

    install_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InstallTime"),
        pydantic.Field(alias="InstallTime", description="The amount of time required to run the package"),
    ] = None
    """
    The amount of time required to run the package
    """

    percentage: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Percentage"),
        pydantic.Field(alias="Percentage", description="The download completion percentage"),
    ] = None
    """
    The download completion percentage
    """

    size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Size"),
        pydantic.Field(alias="Size", description="The total size of the package"),
    ] = None
    """
    The total size of the package
    """

    timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(alias="Timestamp", description="The time the status was last updated"),
    ] = None
    """
    The time the status was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
