from fastapi import APIRouter

router = APIRouter()

router.post("/ask/")
async def ask_question(request: AskModel, db: Session = Depends(get_db)):
    try:
        similar_chunks = await get_similar_chunks(request.document_id, request.question, db)
        
        # Construct context from the similar chunks' texts
        context_texts = [chunk.chunk_text for chunk in similar_chunks]
        context = " ".join(context_texts)

        system_message = f"You are a helpful assistant. Here is the context to use to reply to questions: {context}"

        client = OpenAI(api_key=OPENAI_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.question},
            ]
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
