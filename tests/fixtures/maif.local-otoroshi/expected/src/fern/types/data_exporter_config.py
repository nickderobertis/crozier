

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_exporter_config_config import DataExporterConfigConfig
from .data_exporter_config_typ import DataExporterConfigTyp
from .filtering import Filtering
from .location import Location


class DataExporterConfig(UniversalBaseModel):
    """
    Settings to export Otorshi events
    """

    buffer_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="bufferSize")] = pydantic.Field(
        default=None
    )
    """
    buffer size
    """

    config: typing.Optional[DataExporterConfigConfig] = pydantic.Field(default=None)
    """
    Data Exporter config
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description
    """

    enabled: typing.Optional[str] = pydantic.Field(default=None)
    """
    Boolean
    """

    filtering: typing.Optional[Filtering] = pydantic.Field(default=None)
    """
    filtering
    """

    group_duration: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupDuration")] = (
        pydantic.Field(default=None)
    )
    """
    duration
    """

    group_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupSize")] = pydantic.Field(
        default=None
    )
    """
    Group size
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id
    """

    json_workers: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="jsonWorkers")] = (
        pydantic.Field(default=None)
    )
    """
    nb workers
    """

    location: typing.Optional[Location] = pydantic.Field(default=None)
    """
    location
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Metadata
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name
    """

    projection: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    projection
    """

    send_workers: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sendWorkers")] = (
        pydantic.Field(default=None)
    )
    """
    send workers
    """

    typ: typing.Optional[DataExporterConfigTyp] = pydantic.Field(default=None)
    """
    Type of data exporter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
