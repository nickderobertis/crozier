

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreBrowseFilterFailure(UniversalBaseModel):
    already_owned: typing.Optional[bool] = None
    demo_for_owned_game: typing.Optional[bool] = None
    dlc_for_unowned_game: typing.Optional[bool] = None
    excluded_content_descriptorids: typing.Optional[typing.List[int]] = None
    excluded_tagids: typing.Optional[typing.List[int]] = None
    filter_failure: typing.Optional[int] = None
    ignored: typing.Optional[bool] = None
    nonpreferred_product_type: typing.Optional[bool] = None
    not_in_users_language: typing.Optional[bool] = None
    not_on_users_platform: typing.Optional[bool] = None
    on_wishlist: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
