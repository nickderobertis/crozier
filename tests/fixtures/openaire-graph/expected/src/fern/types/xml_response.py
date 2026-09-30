

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_header import XmlHeader
from .xml_results import XmlResults


class XmlResponse(UniversalBaseModel):
    header: typing.Optional[XmlHeader] = None
    results: typing.Optional[XmlResults] = None
    browse_results: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="browseResults"), pydantic.Field(alias="browseResults")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
