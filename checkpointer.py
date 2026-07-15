from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv
load_dotenv()
import os 

checkpointers=PostgresSaver.from_conn_string(os.get_env("DATABASE_URL"))

