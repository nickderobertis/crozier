

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_provider import ConnectorProvider


class ConnectorProviderCatalogEntry(UniversalBaseModel):
    id: ConnectorProvider
    name: str
    detail_fields: typing.List[str]
    credential_fields: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
