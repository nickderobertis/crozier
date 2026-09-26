

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespaces_get_error500error import NamespacesGetError500Error
from .namespaces_get_error500meta import NamespacesGetError500Meta


class NamespacesGetError500(UniversalBaseModel):
    success: bool
    error: NamespacesGetError500Error
    meta: typing.Optional[NamespacesGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
