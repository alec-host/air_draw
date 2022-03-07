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
	
	class Config:
		orm_mode = True
		
class DrawFinalPoolEntries(CreateAndUpdateDrawFinalPoolEntries):
    _id: int
	
	class Config:
		orm_mode = True

class CreateAndUpdateDrawWinners(BaseModel):
	msisdn: str
	name: str
	ticket_no: str
	tier: Optional[int] = 0
	
	class Config:
		orm_mode = True

class DrawWinners(CreateAndUpdateDrawWinners):
    _id: int

    class Config:
        orm_mode = True