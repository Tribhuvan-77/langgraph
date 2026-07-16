from mem0 import MemoryClient
from dotenv import load_dotenv
load_dotenv()
import os
from app import id


client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

def add_memory(state):

    if state.deployment_status==True:
        messages=[{"role":"user","content":state.design_doc},{"role":"assistant","content":state.code}]
        client.add(messages,user_id=id)
    elif state.design_status=="approved":
        messages=[{"role":"user","content":state.user_story},{"role":"assistant","content":state.design_doc}]
        client.add(messages,user_id=id)
    elif state.story_status=="approved":
        messages=[{"role":"user","content":state.user_input},{"role":"assistant","content":state.user_story}]
        client.add(messages,user_id=id)       
 
