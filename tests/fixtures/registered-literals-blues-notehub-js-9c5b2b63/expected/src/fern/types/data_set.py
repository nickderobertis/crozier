

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_set_field import DataSetField


class DataSet(UniversalBaseModel):
    fields: typing.Optional[typing.List[DataSetField]] = None
    is_optimized: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True once the dataset's underlying table has been deduplicated/optimized. Server-populated; ignored on input.
    """

    is_ready: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True once the dataset has been fully loaded from the repository's archive after backfill completed. Server-populated; ignored on input.
    """

    lat: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSONata expression resulting in the latitude field
    """

    lon: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSONata expression resulting in the Longitude field
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the data set
    """

    notefiles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If non-empty, only events from these notefiles populate the dataset. Empty or omitted means all notefiles.
    """

    time: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSONata expression resulting in the relevant time field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
