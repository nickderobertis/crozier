

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespaces_get_response_data import NamespacesGetResponseData
from .namespaces_get_response_meta import NamespacesGetResponseMeta


class NamespacesGetResponse(UniversalBaseModel):
    success: bool
    data: NamespacesGetResponseData
    meta: typing.Optional[NamespacesGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
