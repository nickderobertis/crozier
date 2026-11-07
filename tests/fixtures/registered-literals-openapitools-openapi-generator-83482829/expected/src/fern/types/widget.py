

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .shape import Shape


class Widget(UniversalBaseModel):
    """
    A Widget demonstrating every OAS 3.1 null-type pattern that the C# generator must handle correctly.
    """

    id: int = pydantic.Field()
    """
    Unique identifier.
    """

    name: str = pydantic.Field()
    """
    Widget name.
    """

    debug_info: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="debugInfo"),
        pydantic.Field(alias="debugInfo", description="Always null in production. Maps to nullable Object in C#."),
    ] = None
    """
    Always null in production. Maps to nullable Object in C#.
    """

    shape: typing.Optional[Shape] = pydantic.Field(default=None)
    """
    Optional shape; null when no shape is assigned.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional CSS color string; null when not set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
