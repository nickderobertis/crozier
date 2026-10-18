

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1DeployAFunctionRequestMetadata(UniversalBaseModel):
    entrypoint_path: str
    import_map_path: typing.Optional[str] = None
    static_patterns: typing.Optional[typing.List[str]] = None
    verify_jwt: typing.Optional[bool] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
