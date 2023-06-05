

from pydantic import BaseModel, validator, ValidationError

from contentctl.objects.security_content_object import SecurityContentObject
from contentctl.objects.enums import SecurityContentType


class Macro(SecurityContentObject):
    contentType: SecurityContentType = SecurityContentType.macros
    #name: str
    definition: str
    #description: str
    arguments: list = None

    # Macro can have different punctuatuation in it,
    # so redefine the name validator. For now, jsut
    # allow any characters in the macro
    @validator('name',check_fields=False)
    def name_invalid_chars(cls, v):
        return v