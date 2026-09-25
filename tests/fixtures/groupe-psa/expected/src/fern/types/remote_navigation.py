

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point import Point


class RemoteNavigation(UniversalBaseModel):
    """
    A remote to share GPS positions with the vehicle so it can navigate through those positions by driving from start (1st) to end (last) position. It can include only 9 points + the destination.
    """

    driver_approval: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="driverApproval"),
        pydantic.Field(
            alias="driverApproval", description="Whether sharing position with vehicle requires driver approval or not."
        ),
    ] = None
    """
    Whether sharing position with vehicle requires driver approval or not.
    """

    positions: typing.List[Point]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
