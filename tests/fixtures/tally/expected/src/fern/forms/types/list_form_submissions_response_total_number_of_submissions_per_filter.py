

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter(UniversalBaseModel):
    all_: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="all"),
        pydantic.Field(alias="all", description="Total number of all submissions"),
    ] = None
    """
    Total number of all submissions
    """

    completed: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of completed submissions
    """

    partial: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of partial submissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
