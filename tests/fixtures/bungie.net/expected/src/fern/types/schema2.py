

Schema2 = int
"""
Represents the possible components that can be returned from Destiny "Get" calls such as GetProfile, GetCharacter, GetVendor etc...
When making one of these requests, you will pass one or more of these components as a comma separated list in the "?components=" querystring parameter. For instance, if you want baseline Profile data, Character Data, and character progressions, you would pass "?components=Profiles,Characters,CharacterProgressions" You may use either the numerical or string values.
"""
