

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_webhooks_response_list_item import ListAllWebhooksResponseListItem


class ListAllWebhooksResponse(UniversalBaseModel):
    page: typing.Optional[int] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[ListAllWebhooksResponseListItem]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
