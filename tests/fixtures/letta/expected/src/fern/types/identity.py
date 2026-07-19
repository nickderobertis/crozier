

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identity_property import IdentityProperty
from .identity_type import IdentityType


class Identity(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Identity
    """

    identifier_key: str = pydantic.Field()
    """
    External, user-generated identifier key of the identity.
    """

    name: str = pydantic.Field()
    """
    The name of the identity.
    """

    identity_type: IdentityType = pydantic.Field()
    """
    The type of the identity.
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The project id of the identity, if applicable.
    """

    agent_ids: typing.List[str] = pydantic.Field()
    """
    The IDs of the agents associated with the identity.
    """

    block_ids: typing.List[str] = pydantic.Field()
    """
    The IDs of the blocks associated with the identity.
    """

    properties: typing.Optional[typing.List[IdentityProperty]] = pydantic.Field(default=None)
    """
    List of properties associated with the identity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
