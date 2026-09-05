

import typing

from .default_keyword_list_upsert_request_partial import DefaultKeywordListUpsertRequestPartial
from .keyword_upsert_request_partial import KeywordUpsertRequestPartial
from .mention_spam_upsert_request_partial import MentionSpamUpsertRequestPartial
from .ml_spam_upsert_request_partial import MlSpamUpsertRequestPartial

UpdateAutoModerationRuleRequestBody = typing.Union[
    DefaultKeywordListUpsertRequestPartial,
    KeywordUpsertRequestPartial,
    MlSpamUpsertRequestPartial,
    MentionSpamUpsertRequestPartial,
]
