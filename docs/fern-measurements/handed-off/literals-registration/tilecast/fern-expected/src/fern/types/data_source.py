

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_source_provider import DataSourceProvider


class DataSource(UniversalBaseModel):
    id: str
    provider: DataSourceProvider
    name: str
    description: typing.Optional[str] = None
    config_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="configVersion"), pydantic.Field(alias="configVersion")
    ]
    configuration: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
