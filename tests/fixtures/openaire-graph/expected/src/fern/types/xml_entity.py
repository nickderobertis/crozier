

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_project import XmlProject
from .xml_publication_result import XmlPublicationResult


class XmlEntity(UniversalBaseModel):
    project: typing.Optional[XmlProject] = None
    result: typing.Optional[XmlPublicationResult] = None
    xmlns_oaf: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xmlnsOaf"), pydantic.Field(alias="xmlnsOaf")
    ] = None
    xsi_schema_location: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xsiSchemaLocation"), pydantic.Field(alias="xsiSchemaLocation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
