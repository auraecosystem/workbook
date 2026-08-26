import sys
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict, List

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Global model container
model_store: Dict[str, Any] = {}
MODEL_PATH = Path("congen-ai/models/stacking_lifespan.pkl")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model into memory on server startup and release on shutdown."""
    if not MODEL_PATH.exists():
        print(f"Error: Model file not found at '{MODEL_PATH.resolve()}'")
    else:
        try:
            model_store["model"] = joblib.load(MODEL_PATH)
            print(f"Successfully loaded model from {MODEL_PATH}")
        except Exception as e:
            print(f"Failed to load model: {e}")
    yield
    model_store.clear()


app = FastAPI(
    title="Lifespan Prediction API",
    description="FastAPI service for serving predictions from stacking_lifespan.pkl",
    version="1.0.0",
    lifespan=lifespan,
)


class LifespanInput(BaseModel):
    """Define features expected by the stacking model.

    Replace/expand fields to match your exact model features.
    """

    feature_1: float = Field(..., example=0.45, description="Primary feature value")
    feature_2: float = Field(..., example=1.28, description="Secondary feature value")
    # Add additional features here matching the training dataset schema


class BatchLifespanInput(BaseModel):
    inputs: List[LifespanInput]


class PredictionOutput(BaseModel):
    predicted_lifespan: float


class BatchPredictionOutput(BaseModel):
    predictions: List[float]


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint to verify API and model state."""
    model_loaded = "model" in model_store
    return {
        "status": "healthy" if model_loaded else "unhealthy",
        "model_loaded": model_loaded,
        "model_path": str(MODEL_PATH),
    }


@app.post(
    "/predict",
    response_model=PredictionOutput,
    status_code=status.HTTP_200_OK,
)
def predict(payload: LifespanInput):
    """Predict lifespan for a single sample."""
    if "model" not in model_store:
        raise HTTPException(
            status_code=status.HTTP_53TC_SERVICE_UNAVAILABLE
            if hasattr(status, "HTTP_53TC_SERVICE_UNAVAILABLE")
            else 503,
            detail="Model is not loaded on the server.",
        )

    try:
        # Convert input payload to DataFrame matching scikit-learn expected input
        input_df = pd.DataFrame([payload.model_dump()])
        prediction = model_store["model"].predict(input_df)
        return PredictionOutput(predicted_lifespan=float(prediction[0]))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Inference failed: {str(e)}",
        )


@app.post(
    "/predict/batch",
    response_model=BatchPredictionOutput,
    status_code=status.HTTP_200_OK,
)
def predict_batch(payload: BatchLifespanInput):
    """Predict lifespan for multiple samples in batch."""
    if "model" not in model_store:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded on the server.",
        )

    try:
        input_df = pd.DataFrame([item.model_dump() for item in payload.inputs])
        predictions = model_store["model"].predict(input_df)
        return BatchPredictionOutput(
            predictions=[float(p) for p in predictions]
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Batch inference failed: {str(e)}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
