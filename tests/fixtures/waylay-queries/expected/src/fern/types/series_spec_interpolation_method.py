

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .series_spec_interpolation_method_value import SeriesSpecInterpolationMethodValue


class SeriesSpecInterpolationMethod(UniversalBaseModel):
    """
    Defines whether, and how to treat missing values.

    This can occur in two circumstances when aggregating (setting a sample frequency):
    * missing values: if there are missing (or invalid) values stored for
    a given freq-interval,
    "interpolation" specifies how to compute these.
    * down-sampling: when the specified freq is smaller than the series’
    actual frequency.
    "interpolation" specifies how to compute intermediate values.
    """

    method: str
    value: typing.Optional[SeriesSpecInterpolationMethodValue] = pydantic.Field(default=None)
    """
    Optional parameter value for the interpolation method (see method description).
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional order parameter for the interpolation method (see method description).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
