

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_models_user_right import OtoroshiModelsUserRight


class OtoroshiModelsUserRights(UniversalBaseModel):
    """
    Represent a list of user rights
    """

    rights: typing.Optional[typing.List[OtoroshiModelsUserRight]] = pydantic.Field(default=None)
    """
    Access rights of a user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
