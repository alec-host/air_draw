'''
@author: alec_host
'''

import uuid

from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

from pydantic import BaseModel
from typing import Optional

class CreateAndUpdateDrawEntries(BaseModel):
	period_in_months: str
	package: str
	cost: Optional[float] = 0.00
	entries: Optional[int] = 0
	is_deleted: Optional[int] = 0
	
	class Config:
		orm_mode = True	
	
class DrawEntries(CreateAndUpdateDrawEntries):
    _id: int

    class Config:
        orm_mode = True