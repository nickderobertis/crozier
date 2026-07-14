

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .policy_bundle import PolicyBundle


class PolicyBundleRecord(UniversalBaseModel):
    """
    A policy bundle plus some metadata
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the bundle is currently defined to be used automatically
    """

    created_at: typing.Optional[dt.datetime] = None
    last_updated: typing.Optional[dt.datetime] = None
    policy_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="policyId")] = pydantic.Field(
        default=None
    )
    """
    The bundle's identifier
    """

    policy_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source location of where the policy bundle originated
    """

    policybundle: typing.Optional[PolicyBundle] = None
    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = pydantic.Field(
        default=None
    )
    """
    UserId of the user that owns the bundle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
