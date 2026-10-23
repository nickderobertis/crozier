

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubProjectCreateBodyAcls(UniversalBaseModel):
    """
    The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.
    """

    admins: typing.Optional[typing.List[str]] = None
    viewers: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
