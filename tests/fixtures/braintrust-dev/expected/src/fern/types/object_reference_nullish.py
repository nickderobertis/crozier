

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .object_reference_nullish_object_type import ObjectReferenceNullishObjectType


class ObjectReferenceNullish(UniversalBaseModel):
    """
    Indicates the event was copied from another object.
    """

    object_type: ObjectReferenceNullishObjectType = pydantic.Field()
    """
    Type of the object the event is originating from.
    """

    object_id: str = pydantic.Field()
    """
    ID of the object the event is originating from.
    """

    id: str = pydantic.Field()
    """
    ID of the original event.
    """

    xact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="_xact_id"),
        pydantic.Field(alias="_xact_id", description="Transaction ID of the original event."),
    ] = None
    """
    Transaction ID of the original event.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    Created timestamp of the original event. Used to help sort in the UI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
