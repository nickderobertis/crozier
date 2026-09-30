

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity import Entity
from .identifier import Identifier


class Node(UniversalBaseModel):
    identifiers: typing.Optional[typing.List[Identifier]] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None
    instance_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="instanceType"), pydantic.Field(alias="instanceType")
    ] = None
    publication_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicationDate"), pydantic.Field(alias="publicationDate")
    ] = None
    authors: typing.Optional[typing.List[Entity]] = None
    collected_from: typing_extensions.Annotated[
        typing.Optional[typing.List[Entity]],
        FieldMetadata(alias="collectedFrom"),
        pydantic.Field(alias="collectedFrom"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
