

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Link(UniversalBaseModel):
    """
    A link between objects.
    """

    uuid_: typing_extensions.Annotated[
        str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="The UUID of this link.")
    ]
    """
    The UUID of this link.
    """

    device: str = pydantic.Field()
    """
    The Device which published this link.
    """

    source: str = pydantic.Field()
    """
    The UUID of the source of the link.
    """

    relation: str = pydantic.Field()
    """
    A UUID identifying the semantics of the link.
    """

    target: str = pydantic.Field()
    """
    The UUID of the target of the link.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
