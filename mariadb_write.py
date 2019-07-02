from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql+pymysql://user:@10.237.89.240/rtpa', echo = True)



def database_entry(min_days,max_days):
	import sqlalchemy as db


	from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,func,select
	engine = create_engine('mysql+pymysql://user:@10.237.89.240/rtpa', echo = False)
	connection = engine.connect()
	metadata = db.MetaData()
	oceane = db.Table('ticket', metadata, autoload=True, autoload_with=engine)
	'''print(oceane.columns.keys())'''
	#Equivalent to 'SELECT * FROM census'
	'''query = db.select([oceane]).where(oceane.columns.first_team == 'proactive')
	query=db.select([func.count()]).select_from(oceane).where  (oceane.columns.first_team == 'proactive') '''
	query=db.select([func.count()]).select_from(oceane).where (oceane.columns.last_update_diff_days.between(min_days,max_days)).\
        group_by('first_team')
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	try:
		print(ResultSet[0][0])
	except:
		ResultSet=[('',), ('',), ('',)]

	print(ResultSet)
	return(ResultSet)


def database_entry_individual(min_days,max_days):
	import sqlalchemy as db


	from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,func,select
	engine = create_engine('mysql+pymysql://user:@10.237.89.240/rtpa', echo = False)
	connection = engine.connect()
	metadata = db.MetaData()
	oceane = db.Table('ticket', metadata, autoload=True, autoload_with=engine)
	'''print(oceane.columns.keys())'''
	#Equivalent to 'SELECT * FROM census'
	'''query = db.select([oceane]).where(oceane.columns.first_team == 'proactive')
	query=db.select([func.count()]).select_from(oceane).where  (oceane.columns.first_team == 'proactive') '''
	query=db.select([func.count()]).select_from(oceane).where (oceane.columns.last_update_diff_days.between(min_days,max_days)).\
        group_by('last_update_by')
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	try:
		print(ResultSet[0][0])
	except:
		ResultSet=[('',), ('',), ('',)]

	print(ResultSet)
	return(ResultSet)




def ticket_create(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step):
	meta = MetaData()
	table_id = Table(
   'ticket', meta, 

   Column('sid', Integer, primary_key = True), 
   Column('incident_no', String(255)), 
   Column('tittle', String(255)), 
   Column('service', String(255)), 
   Column('country', String(255)),
   Column('city', String(255)),
   Column('stype', String(255)), 
   Column('impact', String(255)), 
   Column('status', String(255)),
   Column('action_taken', String(255)),

)
	ins = table_id.insert()
	values_list = [{'incident_no':incident_no,  'tittle': tittle,'service':layer,'country':country ,   'city': city,   'stype':rtpa_type,    'impact': impact, 'status':'Open','action_taken':action_taken }]
	'''values_list=[({'incident_no':a})]'''
	conn = engine.connect()
	result = conn.execute(ins,values_list)





 
def ticket_update(incident_no,action_taken):
	meta = MetaData()
	table_id = Table(
   'comment', meta, 

   Column('sid', Integer, primary_key = True), 
   Column('incident_no', String(255)), 
   Column('action_taken', String(255)), 
 
)
	ins = table_id.insert()
	values_list = [{'incident_no':incident_no,  'action_taken':action_taken }]
	'''values_list=[({'incident_no':a})]'''
	conn = engine.connect()
	result = conn.execute(ins,values_list)


