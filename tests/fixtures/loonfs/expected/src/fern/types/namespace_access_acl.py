

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_grants import AccessGrants
from .principal_scope import PrincipalScope


class NamespaceAccessAcl(UniversalBaseModel):
    """
    Access rows control every operation.
    """

    principal_scope: PrincipalScope = pydantic.Field()
    """
    The identity domain that the namespace's principal IDs belong to.
    """

    root_grants: AccessGrants = pydantic.Field()
    """
    The root inode's grants when the namespace is created. Usually each initial
    administrator has `admin`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
