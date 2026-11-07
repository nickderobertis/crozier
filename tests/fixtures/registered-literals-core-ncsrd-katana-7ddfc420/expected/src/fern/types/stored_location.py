

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StoredLocation(UniversalBaseModel):
    """
    Descriptor of a stored location
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for this location
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A brief description of this location
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="created at"), pydantic.Field(alias="created at")
    ] = None
    vims: typing.Optional[typing.List[str]] = None
    functions: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
