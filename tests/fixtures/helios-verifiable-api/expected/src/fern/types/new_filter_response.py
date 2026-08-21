

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .new_filter_response_kind import NewFilterResponseKind
from .uint import Uint


class NewFilterResponse(UniversalBaseModel):
    id: typing.Optional[Uint] = pydantic.Field(default=None)
    """
    Filter identifier
    """

    kind: typing.Optional[NewFilterResponseKind] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
