

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CredentialParameterYaml(UniversalBaseModel):
    key: str
    description: typing.Optional[str] = None
    credential_id: str
    credential_ids: typing.Optional[typing.List[str]] = None
    selection_strategy: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
