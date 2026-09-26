

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .acquisition_type import AcquisitionType


class Acquisition(UniversalBaseModel):
    """
    Information on how the data was obtained.
    """

    type: AcquisitionType = pydantic.Field()
    """
    The method to obtain the data.
    """

    date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    A string representation of the acquisition datetime in ISO 8601 format.
    """

    link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the data source of this document.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size in bytes of the raw document from the data source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
