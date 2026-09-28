

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsDataExporterConfig(UniversalBaseModel):
    """
    ???
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    buffer_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bufferSize"), pydantic.Field(alias="bufferSize", description="???")
    ] = None
    """
    ???
    """

    json_workers: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="jsonWorkers"), pydantic.Field(alias="jsonWorkers", description="???")
    ] = None
    """
    ???
    """

    group_duration: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="groupDuration"),
        pydantic.Field(alias="groupDuration", description="???"),
    ] = None
    """
    ???
    """

    group_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupSize"), pydantic.Field(alias="groupSize", description="???")
    ] = None
    """
    ???
    """

    type: typing.Optional[typing.Any] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    send_workers: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sendWorkers"), pydantic.Field(alias="sendWorkers", description="???")
    ] = None
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    config: typing.Optional[typing.Any] = None
    projection: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    ???
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    filtering: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
