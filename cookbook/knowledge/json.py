from pathlib import Path

from phi.assistant import Assistant
from phi.knowledge.json import JSONKnowledgeBase
from phi.vectordb.pgvector import PgVector2

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"


# Initialize the JSONKnowledgeBase
knowledge_base = JSONKnowledgeBase(
    path=Path("data/docs"),  # Table name: ai.json_documents
    vector_db=PgVector2(
        collection="json_documents",
        db_url=db_url,
    ),
    num_documents=5,  # Number of documents to return on search
)
# Load the knowledge base
knowledge_base.load(recreate=False)

# Initialize the Assistant with the knowledge_base
assistant = Assistant(
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
)

# Use the assistant
assistant.print_response("Ask me about something from the knowledge base", markdown=True)
