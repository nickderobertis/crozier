

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.serialization import FieldMetadata
from ...types.policy_config import PolicyConfig


class GetPoliciesResponseItem(PolicyConfig):
    user_roles: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="userRoles"), pydantic.Field(alias="userRoles")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
