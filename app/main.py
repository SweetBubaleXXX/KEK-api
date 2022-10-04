import logging

from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.responses import StreamingResponse
from KEK import __version__, exceptions
from KEK.hybrid import PublicKEK

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/version")
async def version():
    return {
        "version": __version__,
    }

@app.post("/encrypt")
async def encrypt(input_file: UploadFile, serialized_key: UploadFile):
    key_bytes = await serialized_key.read()
    try:
        public_key = PublicKEK.load(key_bytes)
    except exceptions.KeyLoadingError:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid key")
    return StreamingResponse(
        public_key.encrypt_chunks(input_file.file),
        media_type="application/octet-stream",
        headers={'Content-Disposition': f'filename={input_file.filename}.kek'}
    )
