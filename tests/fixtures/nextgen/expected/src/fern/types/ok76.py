

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok76(UniversalBaseModel):
    resource_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ]
    base_url: typing_extensions.Annotated[str, FieldMetadata(alias="baseUrl"), pydantic.Field(alias="baseUrl")]
    resource_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="resourceUrl"), pydantic.Field(alias="resourceUrl")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
