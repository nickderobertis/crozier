

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .principal_scope import PrincipalScope


class NamespaceAccessMode_Acl(UniversalBaseModel):
    """
    A namespace's access mode, without the grants that the namespace was created with.
    """

    kind: typing.Literal["acl"] = "acl"
    principal_scope: PrincipalScope

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NamespaceAccessMode_Unrestricted(UniversalBaseModel):
    """
    A namespace's access mode, without the grants that the namespace was created with.
    """

    kind: typing.Literal["unrestricted"] = "unrestricted"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NamespaceAccessMode = typing_extensions.Annotated[
    typing.Union[NamespaceAccessMode_Acl, NamespaceAccessMode_Unrestricted], pydantic.Field(discriminator="kind")
]
