from fastapi import FastAPI,Depends
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes
from users.routes import router as users_routes

tags_metadata = [
    {
        "name": "tasks",
        "description": "Operations related to task management",
        "externalDocs": {
            "description": "More about tasks",
            "url": "https://example.com/docs/tasks"
        }
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")


app = FastAPI(
    title="Todo Application",
    description=(
        "A simple and efficient Todo management API built with FastAPI. "
        "This API allows users to create, retrieve, update, and delete tasks. "
        "It is designed for task tracking and productivity improvement."
    ),
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Ali Bigdeli",
        "url": "https://thealibigdeli.ir",
        "email": "bigdeli.ali3@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }, lifespan=lifespan, openapi_tags=tags_metadata)

app.include_router(tasks_routes)
app.include_router(users_routes)
