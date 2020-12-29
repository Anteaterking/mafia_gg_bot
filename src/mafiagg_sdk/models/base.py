from dataclasses import dataclass, fields
from plistlib import Dict
from typing import Type

import inflection


@dataclass
class Base:
    @classmethod
    def from_json(cls, data: Dict) -> Type["Base"]:
        public_fields = {f.name: f.type for f in fields(cls) if not f.name.startswith("_")}
        kwargs = {}
        for field_name, field_type in public_fields.items():
            data_name = inflection.camelize(field_name, uppercase_first_letter=False)
            value = data.get(data_name)
            if isinstance(field_type, Base):
                value = field_type.from_json(value)
            kwargs[field_name] = value
        return cls(**kwargs)
