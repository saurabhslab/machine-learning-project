import os

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = FastAPI()
app = application
# Templates folder
templates = Jinja2Templates(directory="templates")


# Home Page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Prediction Form Page
@app.get("/predictdata", response_class=HTMLResponse)
async def predict_data_get(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )


# Prediction Endpoint
@app.post("/predictdata", response_class=HTMLResponse)
async def predict_datapoint(
    request: Request,
    gender: str = Form(...),
    ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    writing_score: float = Form(...),
    reading_score: float = Form(...)
):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return templates.TemplateResponse(
            request=request,
            name="home.html",
            context={
                "results": results[0]
            }
        )

    except Exception as e:
        return templates.TemplateResponse(
            request=request,
            name="home.html",
            context={
                "error": str(e)
            }
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5001"))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=os.getenv("RELOAD", "false").lower() == "true"
    )