

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_all_accounts_response_links_first import GetAllAccountsResponseLinksFirst
from .get_all_accounts_response_links_last import GetAllAccountsResponseLinksLast
from .get_all_accounts_response_links_next import GetAllAccountsResponseLinksNext
from .get_all_accounts_response_links_prev import GetAllAccountsResponseLinksPrev
from .get_all_accounts_response_links_self import GetAllAccountsResponseLinksSelf


class GetAllAccountsResponseLinks(UniversalBaseModel):
    first: typing.Optional[GetAllAccountsResponseLinksFirst] = None
    last: typing.Optional[GetAllAccountsResponseLinksLast] = None
    next: typing.Optional[GetAllAccountsResponseLinksNext] = None
    prev: typing.Optional[GetAllAccountsResponseLinksPrev] = None
    self_: typing_extensions.Annotated[
        typing.Optional[GetAllAccountsResponseLinksSelf], FieldMetadata(alias="self"), pydantic.Field(alias="self")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
