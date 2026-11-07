

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dashboard import Dashboard
from .labels import Labels


class DashboardUpdateRequest(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The dashboard name, which is displayed at the top of the dashboard and in lists.
    It does not need to be unique.
    """

    definition: Dashboard
    labels: typing.Optional[Labels] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
