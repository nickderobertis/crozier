

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleIamV1TestIamPermissionsResponse(UniversalBaseModel):
    """
    Response message for `TestIamPermissions` method.
    """

    permissions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A subset of `TestPermissionsRequest.permissions` that the caller is
    allowed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
