

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1forecast_project_client import V1ForecastProjectClient


class V1ForecastProject(UniversalBaseModel):
    """
    Project this task belongs to
    """

    id: int
    active: bool
    name: str
    color: str
    client: V1ForecastProjectClient
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
