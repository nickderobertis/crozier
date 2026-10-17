

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .branch_detail_response_output_status import BranchDetailResponseOutputStatus


class BranchDetailResponseOutput(UniversalBaseModel):
    ref: str
    postgres_version: str
    postgres_engine: str
    release_channel: str
    status: BranchDetailResponseOutputStatus
    db_host: str
    db_port: int
    db_user: typing.Optional[str] = None
    db_pass: typing.Optional[str] = None
    jwt_secret: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
