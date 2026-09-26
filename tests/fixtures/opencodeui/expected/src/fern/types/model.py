

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_api import ModelApi
from .model_capabilities import ModelCapabilities
from .model_cost import ModelCost
from .model_limit import ModelLimit
from .model_status import ModelStatus


class Model(UniversalBaseModel):
    id: str
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerID"), pydantic.Field(alias="providerID")]
    api: ModelApi
    name: str
    family: typing.Optional[str] = None
    capabilities: ModelCapabilities
    cost: ModelCost
    limit: ModelLimit
    status: ModelStatus
    options: typing.Dict[str, typing.Any]
    headers: typing.Dict[str, str]
    release_date: str
    variants: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
