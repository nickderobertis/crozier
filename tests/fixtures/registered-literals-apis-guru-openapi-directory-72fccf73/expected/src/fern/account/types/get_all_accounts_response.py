

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.get_all_account_response import GetAllAccountResponse
from .get_all_accounts_response_links import GetAllAccountsResponseLinks


class GetAllAccountsResponse(UniversalBaseModel):
    embedded: typing_extensions.Annotated[
        typing.Optional[typing.List[GetAllAccountResponse]],
        FieldMetadata(alias="_embedded"),
        pydantic.Field(alias="_embedded"),
    ] = None
    links: typing_extensions.Annotated[
        typing.Optional[GetAllAccountsResponseLinks], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ] = None
    page_number: typing.Optional[int] = None
    page_size: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
