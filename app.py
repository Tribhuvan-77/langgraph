
from uuid import uuid4
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv
import os
from sdlc_graph import graph

load_dotenv()

DB_URI = os.getenv("DATABASE_URL")

id=str(uuid4())


def main():
    with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
     checkpointer.setup()
     a=graph.compile(checkpointer=checkpointer)
     user_input = input()
     result = a.invoke({"user_input": user_input,"user_id":id},config={"configurable": {"thread_id":id}})
     print(result)


if __name__ == "__main__":
    main()