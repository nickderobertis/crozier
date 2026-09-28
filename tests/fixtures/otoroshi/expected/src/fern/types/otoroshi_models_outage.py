

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsOutage(UniversalBaseModel):
    """
    ???
    """

    descriptor_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="descriptorName"),
        pydantic.Field(alias="descriptorName", description="???"),
    ] = None
    """
    ???
    """

    descriptor_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="descriptorId"),
        pydantic.Field(alias="descriptorId", description="???"),
    ] = None
    """
    ???
    """

    until: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    ???
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt", description="???")
    ] = None
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
