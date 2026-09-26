

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provider_list_response_all_item import ProviderListResponseAllItem


class ProviderListResponse(UniversalBaseModel):
    all_: typing_extensions.Annotated[
        typing.List[ProviderListResponseAllItem], FieldMetadata(alias="all"), pydantic.Field(alias="all")
    ]
    default: typing.Dict[str, str]
    connected: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
