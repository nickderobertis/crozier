

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentJavaPackageResponseContentItem(UniversalBaseModel):
    cpes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of Common Platform Enumerations that may uniquely identify the package
    """

    implementation_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="implementation-version"),
        pydantic.Field(alias="implementation-version"),
    ] = None
    location: typing.Optional[str] = None
    maven_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="maven-version"), pydantic.Field(alias="maven-version")
    ] = None
    origin: typing.Optional[str] = None
    package: typing.Optional[str] = None
    specification_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="specification-version"),
        pydantic.Field(alias="specification-version"),
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
