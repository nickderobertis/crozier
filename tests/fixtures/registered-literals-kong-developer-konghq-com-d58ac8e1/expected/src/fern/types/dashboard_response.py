

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .dashboard import Dashboard
from .labels import Labels
from .updated_at import UpdatedAt
from .uuid_ import Uuid


class DashboardResponse(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The dashboard name, which is displayed at the top of the dashboard and in lists.
    It does not need to be unique.
    """

    definition: Dashboard
    labels: typing.Optional[Labels] = None
    id: typing.Optional[Uuid] = None
    created_by: typing.Optional[Uuid] = None
    created_at: typing.Optional[CreatedAt] = None
    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
