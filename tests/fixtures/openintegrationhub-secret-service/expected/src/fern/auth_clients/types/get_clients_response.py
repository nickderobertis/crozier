

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.auth_client_entry import AuthClientEntry
from ...types.meta import Meta


class GetClientsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AuthClientEntry]] = None
    meta: typing.Optional[Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
