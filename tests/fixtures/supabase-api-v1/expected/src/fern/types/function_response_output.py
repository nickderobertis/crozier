

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_response_output_status import FunctionResponseOutputStatus


class FunctionResponseOutput(UniversalBaseModel):
    id: str
    slug: str
    name: str
    status: FunctionResponseOutputStatus
    version: int
    created_at: int
    updated_at: int
    verify_jwt: typing.Optional[bool] = None
    import_map: typing.Optional[bool] = None
    entrypoint_path: typing.Optional[str] = None
    import_map_path: typing.Optional[str] = None
    ezbr_sha256: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
