

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monitor_trigger import MonitorTrigger


class MonitorParameterTriggerParam(UniversalBaseModel):
    """
    Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.
    """

    triggers: typing.List[MonitorTrigger] = pydantic.Field()
    """
    Compound monitor triggers (will be evaluated using boolean expresion :```booExp```). At least, ```one``` trigger should be provided and at  most, ```five``` items are accepted.
    """

    bool_exp: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="boolExp"),
        pydantic.Field(
            alias="boolExp",
            description="A boolean expression that allow defining a logical relationship between triggers. Used Operands with this expression should be the names of the defined triggers. \n \n  _Note:_ Always ```true``` or Always```false``` expression are prohibited and will result with an http 400 error response.\n  \n  \nGrammar:\n```\nexp ::= exp '&' exp\n       | exp '|' exp\n       | (exp)\n       | !exp\n```\n\n* **example**: having two-zone trigger (two towns) named z1 an z2, one time-trigger (8h00 to 20h00) named t1 and finally three data triggerd named as follow: f(fuel), a(autonomy) , o(odometer).\n  \n  we can have a boolean expression such as: : ``` ((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2))) ```",
        ),
    ]
    """
    A boolean expression that allow defining a logical relationship between triggers. Used Operands with this expression should be the names of the defined triggers. 
     
      _Note:_ Always ```true``` or Always```false``` expression are prohibited and will result with an http 400 error response.
      
      
    Grammar:
    ```
    exp ::= exp '&' exp
           | exp '|' exp
           | (exp)
           | !exp
    ```
    
    * **example**: having two-zone trigger (two towns) named z1 an z2, one time-trigger (8h00 to 20h00) named t1 and finally three data triggerd named as follow: f(fuel), a(autonomy) , o(odometer).
      
      we can have a boolean expression such as: : ``` ((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2))) ```
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
