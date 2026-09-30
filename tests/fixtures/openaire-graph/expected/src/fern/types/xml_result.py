

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_metadata import XmlMetadata
from .xml_result_header import XmlResultHeader


class XmlResult(UniversalBaseModel):
    header: XmlResultHeader
    metadata: XmlMetadata
    xmlns_dri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xmlnsDri"), pydantic.Field(alias="xmlnsDri")
    ] = None
    xmlns_xsi: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xmlnsXsi"), pydantic.Field(alias="xmlnsXsi")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
