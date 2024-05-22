#export LANGCHAIN_TRACING_V2="true"
#export LANGCHAIN_API_KEY="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"
#export API_KEY="AIzaSyAvMS1PkJBBYql65I_IE_RHeqbjjG0Z7YU"
#api_key = getpass()


#import getpass
import os
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAI

#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
#os.environ["GOOGLE_API_KEY"] = getpass.getpass()
flag_tracing = os.environ["LANGCHAIN_TRACING_V2"]
gg_api_key= os.environ['API_KEY']
lc_api_key = os.environ['LANGCHAIN_API_KEY']

tools = []
model = ChatVertexAI(model="gemini-pro")
#model = GoogleGenerativeAI(model="gemini-pro", google_api_key=gg_api_key)

#response = model.invoke([HumanMessage(content="hi!")])
#response = model.invoke( "Hi")
#print( response.content )

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)