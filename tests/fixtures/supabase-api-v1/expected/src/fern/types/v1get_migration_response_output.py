

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1GetMigrationResponseOutput(UniversalBaseModel):
    version: str
    name: typing.Optional[str] = None
    statements: typing.Optional[typing.List[str]] = None
    rollback: typing.Optional[typing.List[str]] = None
    created_by: typing.Optional[str] = None
    idempotency_key: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
