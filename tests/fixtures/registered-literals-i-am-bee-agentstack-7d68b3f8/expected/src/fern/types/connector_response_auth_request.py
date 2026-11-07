

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectorResponseAuthRequest_Code(UniversalBaseModel):
    type: typing.Literal["code"] = "code"
    authorization_endpoint: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConnectorResponseAuthRequest = ConnectorResponseAuthRequest_Code
