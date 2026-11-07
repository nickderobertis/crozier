

import typing

from .creator_email_model import CreatorEmailModel
from .creator_id_model import CreatorIdModel

CreatorModel = typing.Union[CreatorEmailModel, CreatorIdModel]
