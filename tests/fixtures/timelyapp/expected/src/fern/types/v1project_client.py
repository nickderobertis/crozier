

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1project_client_external_references_item import V1ProjectClientExternalReferencesItem
from .v1project_client_tic import V1ProjectClientTic


class V1ProjectClient(UniversalBaseModel):
    id: int
    name: str
    active: bool
    external_id: typing.Optional[str] = None
    updated_at: dt.datetime
    color: str
    external_references: typing.Optional[typing.List[V1ProjectClientExternalReferencesItem]] = None
    tic: typing.Optional[V1ProjectClientTic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
