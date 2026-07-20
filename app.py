
from uuid import uuid4
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.types import Command
from dotenv import load_dotenv
import os
from sdlc_graph import graph
import asyncio

load_dotenv()

DB_URI = os.getenv("DATABASE_URL")

id=str(uuid4())
config={"configurable": {"thread_id":id}}
   
async def main():
    async with AsyncPostgresSaver.from_conn_string(DB_URI) as checkpointer:
      await checkpointer.setup()
      a=graph.compile(checkpointer=checkpointer)
      user_input = input()
      async for event in a.astream_events({"user_input": user_input,"user_id":id},config=config,version="v2"):
         if event["event"] == "on_chain_start":
          print(event["name"])
      
      
      
    #   decision = input("yes or no?")

    #   async for event in a.astream_events(Command(resume=decision),config=config):
    #      print(event)


if __name__ == "__main__":
    asyncio.run(main())