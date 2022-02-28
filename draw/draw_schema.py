'''
@author: alec_host
'''

import uuid

from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

from pydantic import BaseModel
from typing import Optional

class CreateAndUpdateDrawFinalPoolEntries(BaseModel):
	msisdn: str
	ticket_no: str
	tier: Optional[int] = 0
		
class DrawFinalPoolEntries(CreateAndUpdateDrawFinalPoolEntries):
    _id: int

class CreateAndUpdateDrawWinners(BaseModel):
	msisdn: str
	name: str
	ticket_no: str
	tier: Optional[int] = 0

class DrawWinners(CreateAndUpdateDrawWinners):
    _id: int

    class Config:
        orm_mode = True