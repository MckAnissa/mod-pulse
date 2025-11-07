from __future__ import annotations
import os
from pydantic import BaseModel

class Settings(BaseModel):
    mods_root: str | None = os.getenv("MODS_ROOT")

settings = Settings()
