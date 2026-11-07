

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RouteTransformSettings(UniversalBaseModel):
    """
    Settings for transforming route payloads before delivery. Supports format
    selection and JSONata-based transformations.
    """

    format: typing.Optional[str] = pydantic.Field(default=None)
    """
    Output format for transformed data (e.g., "json", "xml", "text").
    """

    jsonata: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSONata expression used to transform the data payload (outgoing).
    """

    jsonata_in: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSONata expression used to transform the data payload (incoming).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
