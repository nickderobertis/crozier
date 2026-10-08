

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetApiStatusResponse(UniversalBaseModel):
    filenames: typing.Optional[typing.List[str]] = None
    lsp_running: typing.Optional[bool] = None
    mode: typing.Optional[str] = None
    node_version: typing.Optional[str] = None
    requirements: typing.Optional[typing.List[str]] = None
    sessions: typing.Optional[int] = None
    status: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
