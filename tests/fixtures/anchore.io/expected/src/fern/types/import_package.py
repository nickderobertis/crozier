

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .import_package_location import ImportPackageLocation


class ImportPackage(UniversalBaseModel):
    cpes: typing.List[str]
    found_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="foundBy"), pydantic.Field(alias="foundBy")
    ] = None
    id: typing.Optional[str] = None
    language: str
    licenses: typing.List[str]
    locations: typing.List[ImportPackageLocation]
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    metadata_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="metadataType"), pydantic.Field(alias="metadataType")
    ]
    name: str
    purl: typing.Optional[str] = None
    type: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
