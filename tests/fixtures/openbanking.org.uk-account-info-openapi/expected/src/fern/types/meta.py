

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .iso_date_time import IsoDateTime


class Meta(UniversalBaseModel):
    """
    Meta Data relevant to the payload
    """

    first_available_date_time: typing_extensions.Annotated[
        typing.Optional[IsoDateTime],
        FieldMetadata(alias="FirstAvailableDateTime"),
        pydantic.Field(alias="FirstAvailableDateTime"),
    ] = None
    last_available_date_time: typing_extensions.Annotated[
        typing.Optional[IsoDateTime],
        FieldMetadata(alias="LastAvailableDateTime"),
        pydantic.Field(alias="LastAvailableDateTime"),
    ] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="TotalPages"), pydantic.Field(alias="TotalPages")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
