'''
@author: alec_host
'''
import sys
import uuid
import logging

import pytz
import datetime

from sqlalchemy import or_,desc
from sqlalchemy.orm import Session

from register_schema import CreateAndUpdateCustomerEntries
from register_model import CustomerEntriesDescription

import conn.config
sys.path.insert(0,conn.config.UTILITY_DIR)
import uid_generator

logger = logging.getLogger(__name__)

zone = pytz.timezone("Africa/Nairobi")
my_time_zone = zone.localize(datetime.datetime.now(),is_dst=True)

local_now = datetime.datetime.now().astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)

if(local_tzname != 'E. Africa Standard Time'):
	EAT = my_time_zone + datetime.timedelta(hours = 3)
	date = EAT.strftime('%Y-%m-%d %H:%M:%S')
else:
	date = my_time_zone.strftime('%Y-%m-%d %H:%M:%S')

#-.method: create customer entries.
def _customer_payment_details(session: Session, customer_info: CreateAndUpdateCustomerEntries,_entries: int,_tier: int,_validity_in_month: int) -> CustomerEntriesDescription:
	try:
		customer_details = session.query(CustomerEntriesDescription.company_identifier).where(CustomerEntriesDescription.msisdn==customer_info.msisdn,CustomerEntriesDescription.validity_in_month!=1)
		if(int(customer_details.count()) == 0):
			for i in range(_entries):
				new_customer_info = CustomerEntriesDescription(company_name=customer_info.company_name,
															   company_identifier=customer_info.company_identifier,
															   name=customer_info.name,
															   email=customer_info.email,
															   msisdn=customer_info.msisdn,
															   ticket_no='AD_'+uid_generator.get_custom_alpha_uid()+'O',
															   amount=customer_info.amount,
															   package=customer_info.package,
															   tier=_tier,
															   validity_in_month=_validity_in_month,
															   date_created=date,
															   date_modified=date,
															   is_archived=0)

				session.add(new_customer_info)
				session.commit()
				session.refresh(new_customer_info)
				
			new_customer_info=1
			logger.info(new_customer_info)
		else:
			new_customer_info=None
	except Exception as ex:
		logger.debug(ex)
		raise ex
		
	finally:
		session.close()
	
	return new_customer_info
	
#-.method: get customer entries.
def _customer_entries(session: Session,_msisdn: str, _limit: int) -> CustomerEntriesDescription:
	try:
		if(_msisdn == '0'):
			result = session.query(CustomerEntriesDescription._Id,
								   CustomerEntriesDescription.company_name,
								   CustomerEntriesDescription.company_identifier,
								   CustomerEntriesDescription.name,
								   CustomerEntriesDescription.msisdn,
								   CustomerEntriesDescription.ticket_no,
								   CustomerEntriesDescription.amount,
								   CustomerEntriesDescription.package,
								   CustomerEntriesDescription.tier,
								   CustomerEntriesDescription.date_created).\
								   order_by(desc(CustomerEntriesDescription.date_created)).\
								   limit(_limit)
		else:
			result = session.query(CustomerEntriesDescription._Id,
								   CustomerEntriesDescription.company_name,
								   CustomerEntriesDescription.company_identifier,
								   CustomerEntriesDescription.name,
								   CustomerEntriesDescription.msisdn,
								   CustomerEntriesDescription.ticket_no,
								   CustomerEntriesDescription.amount,
								   CustomerEntriesDescription.package,
								   CustomerEntriesDescription.tier,
								   CustomerEntriesDescription.date_created).\
								   where(CustomerEntriesDescription.msisdn==_msisdn).\
								   order_by(desc(CustomerEntriesDescription.date_created)).\
								   limit(_limit)			
	except Exception as ex:
		raise ex
	finally:
		session.close()
		
	return result.all()