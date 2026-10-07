

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetApiEnvironmentResponse(UniversalBaseModel):
    binaries: typing_extensions.Annotated[
        typing.Dict[str, str], FieldMetadata(alias="Binaries"), pydantic.Field(alias="Binaries")
    ]
    dependencies: typing_extensions.Annotated[
        typing.Dict[str, str], FieldMetadata(alias="Dependencies"), pydantic.Field(alias="Dependencies")
    ]
    experimental_flags: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="Experimental Flags"),
        pydantic.Field(alias="Experimental Flags"),
    ]
    locale: typing_extensions.Annotated[str, FieldMetadata(alias="Locale"), pydantic.Field(alias="Locale")]
    os: typing_extensions.Annotated[str, FieldMetadata(alias="OS"), pydantic.Field(alias="OS")]
    os_version: typing_extensions.Annotated[str, FieldMetadata(alias="OS Version"), pydantic.Field(alias="OS Version")]
    optional_dependencies: typing_extensions.Annotated[
        typing.Dict[str, str],
        FieldMetadata(alias="Optional Dependencies"),
        pydantic.Field(alias="Optional Dependencies"),
    ]
    processor: typing_extensions.Annotated[str, FieldMetadata(alias="Processor"), pydantic.Field(alias="Processor")]
    python_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="Python Version"), pydantic.Field(alias="Python Version")
    ]
    editable: bool
    location: str
    marimo: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
