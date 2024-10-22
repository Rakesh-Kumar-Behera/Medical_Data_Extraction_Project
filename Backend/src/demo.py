from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
import uvicorn

app = FastAPI()

# Create a directory for storing uploads if it doesn't exist
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve static files (like the HTML) if necessary
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the webpage (HTML) for file upload
@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Medical Data Extractor</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }

            h1 {
                color: #333;
            }

            select, input[type="file"], input[type="submit"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            input[type="submit"] {
                background-color: #28a745;
                color: white;
                border: none;
                cursor: pointer;
            }

            input[type="submit"]:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Medical Data Extractor</h1>

            <form action="/upload" method="post" enctype="multipart/form-data">
                <!-- Option to select type (Prescription or Patient Details) -->
                <label for="data-type">Select Data Type:</label>
                <select id="data-type" name="data-type" required>
                    <option value="">-- Select Option --</option>
                    <option value="prescription">Prescription</option>
                    <option value="patient-details">Patient Details</option>
                </select>

                <!-- File upload field -->
                <label for="file-upload">Upload a File:</label>
                <input type="file" id="file-upload" name="file" accept=".pdf, .jpg, .jpeg, .png, .txt" required>

                <!-- Submit button to extract data -->
                <input type="submit" value="Extract Data">
            </form>
        </div>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Handle file upload and data extraction
@app.post("/upload")
async def handle_upload(data_type: str = Form(...), file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {
        "message": "File successfully uploaded",
        "file_name": file.filename,
        "data_type": data_type,
        "file_location": file_location
    }

# Run the FastAPI server with: uvicorn app:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
