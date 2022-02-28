import sys
import uuid



from datetime import datetime

from sqlalchemy import or_,desc
from sqlalchemy.orm import Session

from register_schema import CreateAndUpdateCustomerEntries
from register_model import CustomerEntriesDescription

import conn.config
sys.path.insert(0,conn.config.UTILITY_DIR)
import uid_generator

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#customer_entries.company_identifier
#-.method: create customer entries.
def _customer_payment_details(session: Session, customer_info: CreateAndUpdateCustomerEntries,draw_entries: int) -> CustomerEntriesDescription:
	customer_details = session.query(CustomerEntriesDescription.company_identifier).filter(CustomerEntriesDescription.msisdn==customer_info.msisdn)
	if(int(customer_details.count()) == 0):
		#-.generate several entries.
		for i in range(draw_entries):
			new_customer_info = CustomerEntriesDescription(company_name=customer_info.company_name,
														   company_identifier=customer_info.company_identifier,
													       name=customer_info.name,
													       email=customer_info.email,
													       msisdn=customer_info.msisdn,
													       ticket_no='AD_'+uid_generator.get_custom_alpha_uid()+'O',
													       amount=customer_info.amount,
													       package=customer_info.package,
													       tier=customer_info.tier,
													       date_created=date,
													       date_modified=date,
													       is_archived=0)

			session.add(new_customer_info)
			session.commit()
			session.refresh(new_customer_info)
			
		new_customer_info=1
	else:
		new_customer_info=None
	
	return new_customer_info
	

def _customer_list(session: Session,_msisdn: str, _limit: int):
	pass