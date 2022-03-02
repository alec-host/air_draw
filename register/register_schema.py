'''
@author: alec_host
'''
import uuid

from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

from pydantic import BaseModel
from typing import Optional

class CreateAndUpdateCustomerEntries(BaseModel):
	company_name: str
	company_identifier: str
	name: str
	msisdn: str
	email: str
	ticket_no: Optional[float] = 0.00
	amount: Optional[float] = 0.00
	package: str
	tier: str
	date_created: Optional[str] = date
	date_modified: Optional[str] = date
	is_archived: Optional[int] = 0
	
class CreateAndUpdateDrawManifest(BaseModel):
	period_in_months: str
	package: str
	cost: Optional[float] = 0.00
	entries: Optional[int] = 0
	tier: Optional[int] = 0
	is_deleted: Optional[int] = 0
	
class UserCustomerEntries(CreateAndUpdateCustomerEntries):
    msisdn: str

    class Config:
        orm_mode = True
		
class DrawManifest(CreateAndUpdateDrawManifest):
    _id: str

    class Config:
        orm_mode = True