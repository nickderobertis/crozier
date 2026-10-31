

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lineage_activity_status import LineageActivityStatus
from .lineage_association import LineageAssociation
from .lineage_implementation import LineageImplementation


class LineageActivity(UniversalBaseModel):
    """
    An operation that used entities and generated new ones, with implementation, timing, parameters, and responsible agents when known.
    """

    type: str
    name: typing.Optional[str] = None
    status: typing.Optional[LineageActivityStatus] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    ended_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")
    ] = None
    implementation: typing.Optional[LineageImplementation] = None
    parameters: typing.Optional[typing.Dict[str, typing.Any]] = None
    associations: typing.Optional[typing.List[LineageAssociation]] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
