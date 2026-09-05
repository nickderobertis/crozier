

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .encrypted_root_key_str import EncryptedRootKeyStr
from .file_id_str import FileIdStr


class JobEncryptionContextMetadata(UniversalBaseModel):
    encrypted_root_key: EncryptedRootKeyStr
    input_port_to_file_id: typing.Optional[typing.Dict[str, typing.Dict[str, FileIdStr]]] = pydantic.Field(default=None)
    """
    Per computational node, maps each encrypted input port key to the file_id the client used to derive its key (may differ from the port key). Only listed inputs are decrypted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
