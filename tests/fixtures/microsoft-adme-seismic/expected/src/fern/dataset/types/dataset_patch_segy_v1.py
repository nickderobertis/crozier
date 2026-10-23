

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_patch_segy_v1acl import DatasetPatchSegyV1Acl
from .dataset_patch_segy_v1ancestry import DatasetPatchSegyV1Ancestry
from .dataset_patch_segy_v1data import DatasetPatchSegyV1Data
from .dataset_patch_segy_v1legal import DatasetPatchSegyV1Legal
from .dataset_patch_segy_v1meta_item import DatasetPatchSegyV1MetaItem


class DatasetPatchSegyV1(UniversalBaseModel):
    """
    A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previously called ResourceID or SRN which identifies this OSDU resource object without version.
    """

    kind: str = pydantic.Field()
    """
    The schema identification for the OSDU resource object following the pattern {Namespace}:{Source}:{Type}:{VersionMajor}.{VersionMinor}.{VersionPatch}. The versioning scheme follows the semantic versioning, https://semver.org/.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number of this OSDU resource; set by the framework.
    """

    acl: typing.Optional[DatasetPatchSegyV1Acl] = pydantic.Field(default=None)
    """
    The access control tags associated with this entity. This structure is included by the SystemProperties "acl", which is part of all OSDU records. Not extensible.
    """

    legal: typing.Optional[DatasetPatchSegyV1Legal] = pydantic.Field(default=None)
    """
    Legal meta data like legal tags, relevant other countries, legal status. This structure is included by the SystemProperties "legal", which is part of all OSDU records. Not extensible.
    """

    tags: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    A generic dictionary of string keys mapping to string value. Only strings are permitted as keys and values.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createTime"),
        pydantic.Field(
            alias="createTime",
            description="Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
        ),
    ] = None
    """
    Timestamp of the time at which initial version of this OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.
    """

    create_user: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createUser"),
        pydantic.Field(
            alias="createUser",
            description="The user reference, which created the first version of this resource object. Set by the System.",
        ),
    ] = None
    """
    The user reference, which created the first version of this resource object. Set by the System.
    """

    modify_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifyTime"),
        pydantic.Field(
            alias="modifyTime",
            description="Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.",
        ),
    ] = None
    """
    Timestamp of the time at which this version of the OSDU resource object was created. Set by the System. The value is a combined date-time string in ISO-8601 given in UTC.
    """

    modify_user: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modifyUser"),
        pydantic.Field(
            alias="modifyUser",
            description="The user reference, which created this version of this resource object. Set by the System.",
        ),
    ] = None
    """
    The user reference, which created this version of this resource object. Set by the System.
    """

    ancestry: typing.Optional[DatasetPatchSegyV1Ancestry] = pydantic.Field(default=None)
    """
    A list of entity IDs in the data ecosystem, which act as legal parents to the current entity. This structure is included by the SystemProperties "ancestry", which is part of all OSDU records. Not extensible.
    """

    meta: typing.Optional[typing.List[DatasetPatchSegyV1MetaItem]] = pydantic.Field(default=None)
    """
    The Frame of Reference meta data section linking the named properties to self-contained definitions.
    """

    data: typing.Optional[DatasetPatchSegyV1Data] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
