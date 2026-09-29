

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class XmlResultHeader(UniversalBaseModel):
    obj_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="objIdentifier"), pydantic.Field(alias="objIdentifier")
    ] = None
    date_of_collection: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dateOfCollection"), pydantic.Field(alias="dateOfCollection")
    ] = None
    date_of_transformation: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dateOfTransformation"), pydantic.Field(alias="dateOfTransformation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
