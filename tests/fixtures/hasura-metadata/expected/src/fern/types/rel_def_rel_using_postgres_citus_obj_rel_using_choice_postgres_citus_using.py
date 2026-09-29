

import typing

from .citus_ru_manual import CitusRuManual
from .ruf_key_on_obj_rel_using_choice_postgres_citus import RufKeyOnObjRelUsingChoicePostgresCitus

RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing = typing.Union[
    RufKeyOnObjRelUsingChoicePostgresCitus, CitusRuManual
]
