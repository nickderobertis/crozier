

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_grants import AccessGrants
from .principal_scope import PrincipalScope


class NamespaceAccess_Acl(UniversalBaseModel):
    """
    A namespace's access mode, which can't be changed after the namespace is created.
    """

    kind: typing.Literal["acl"] = "acl"
    principal_scope: PrincipalScope
    root_grants: AccessGrants

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NamespaceAccess_Unrestricted(UniversalBaseModel):
    """
    A namespace's access mode, which can't be changed after the namespace is created.
    """

    kind: typing.Literal["unrestricted"] = "unrestricted"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NamespaceAccess = typing_extensions.Annotated[
    typing.Union[NamespaceAccess_Acl, NamespaceAccess_Unrestricted], pydantic.Field(discriminator="kind")
]
