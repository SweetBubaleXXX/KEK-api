from os import getenv

import uvicorn
from fastapi import FastAPI, HTTPException, Response, UploadFile, status
from fastapi.responses import StreamingResponse
from KEK import __version__, exceptions
from KEK.hybrid import PublicKEK

app = FastAPI(
    title="KEK-api",
    description="Public KEK encryption API.",
    version="1.0.0",
    contact={
        "name": "SweetBubaleXXX",
        "url": "https://github.com/SweetBubaleXXX/KEK-api.git"
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html"
    }
)


@app.get("/version")
async def version():
    return {
        "version": __version__,
    }


@app.post(
    "/encrypt",
    response_class=Response,
    responses={
        200: {
            "content": {"application/octet-stream": {}}
        }
    }
)
async def encrypt(input_file: UploadFile, serialized_key: UploadFile):
    key_bytes = await serialized_key.read()
    try:
        public_key = PublicKEK.load(key_bytes)
    except exceptions.KeyLoadingError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid key"
        )
    return StreamingResponse(
        public_key.encrypt_chunks(input_file.file),
        media_type="application/octet-stream",
        headers={'Content-Disposition': f'filename={input_file.filename}.kek'}
    )


if __name__ == "__main__":
    uvicorn.run(
        app, host=getenv("HOST", "0.0.0.0"),
        port=int(getenv("PORT", 8000))
    )
