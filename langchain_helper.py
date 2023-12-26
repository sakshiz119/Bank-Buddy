from langchain.llms import GooglePalm
from langchain.sql_database import SQLDatabase
import langchain_experimental.sql as le

from dotenv import load_dotenv
load_dotenv()

api_key = 'AIzaSyDRTnPJKctIWZg9QThtwkEy--pyDTLZ_Ao'
def db_chain():
    db_user = "root"
    db_password = "11902"
    db_host = "localhost"
    db_name = "bank_db"
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=5)
    llm = GooglePalm(google_api_key=api_key, temperature=0.1)
    chain = le.SQLDatabaseChain(llm=llm, database=db, verbose=True)
    return chain
