

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unified_id import UnifiedId


class DeleteDepartmentResponse(UniversalBaseModel):
    data: UnifiedId
    operation: str = pydantic.Field()
    """
    Operation performed
    """

    resource: str = pydantic.Field()
    """
    Unified API resource name
    """

    service: str = pydantic.Field()
    """
    Apideck ID of service provider
    """

    status: str = pydantic.Field()
    """
    HTTP Response Status
    """

    status_code: int = pydantic.Field()
    """
    HTTP Response Status Code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
