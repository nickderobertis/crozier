

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .series_description import SeriesDescription
from .series_id import SeriesId
from .series_name import SeriesName
from .updated_at import UpdatedAt


class Series(UniversalBaseModel):
    """
    A series object which includes the name and description of the series.
    """

    id: typing.Optional[SeriesId] = None
    name: typing.Optional[SeriesName] = None
    description: typing.Optional[SeriesDescription] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
