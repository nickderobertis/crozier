

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespaces_get_error503error import NamespacesGetError503Error
from .namespaces_get_error503meta import NamespacesGetError503Meta


class NamespacesGetError503(UniversalBaseModel):
    success: bool
    error: NamespacesGetError503Error
    meta: typing.Optional[NamespacesGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
