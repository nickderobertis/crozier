

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identifier import Identifier
from .uuid_ import Uuid


class Component(UniversalBaseModel):
    """
    A TEA component
    """

    uuid_: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="A unique identifier for the TEA component"),
    ]
    """
    A unique identifier for the TEA component
    """

    name: str = pydantic.Field()
    """
    Component name
    """

    identifiers: typing.List[Identifier] = pydantic.Field()
    """
    List of identifiers for the component
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
