

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_dataset_abilities_value import MeDatasetAbilitiesValue
from .me_groups_item import MeGroupsItem


class Me(UniversalBaseModel):
    user_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userName"), pydantic.Field(alias="userName")
    ] = None
    hide_logout_button: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hideLogoutButton"), pydantic.Field(alias="hideLogoutButton")
    ] = None
    dataset_abilities: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, MeDatasetAbilitiesValue]],
        FieldMetadata(alias="datasetAbilities"),
        pydantic.Field(alias="datasetAbilities", description="Per dataset abilities of the logged in User."),
    ] = None
    """
    Per dataset abilities of the logged in User.
    """

    groups: typing.Optional[typing.List[MeGroupsItem]] = pydantic.Field(default=None)
    """
    Groups the user is part of.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
