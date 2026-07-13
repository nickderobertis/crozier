

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_records_destiny_record_component import DestinyComponentsRecordsDestinyRecordComponent


class DestinyComponentsRecordsDestinyCharacterRecordsComponent(UniversalBaseModel):
    featured_record_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="featuredRecordHashes")
    ] = None
    record_categories_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordCategoriesRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Triumph categories.
    """

    record_seals_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordSealsRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Triumph Seals.
    """

    records: typing.Optional[typing.Dict[str, DestinyComponentsRecordsDestinyRecordComponent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
