# Mining Digital Twin

Mining Digital Twin Frontend GUI built with Streamlit.

## Pages
1. Executive Overview
2. Live Process Twin
3. Unit Operations
4. Simulation WhatIf
5. Optimization
6. Control Advisory
7. Asset Health
8. Data Quality
9. Admin Config

## Local Development Setup
```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Environment Variables
- `BACKEND_BASE_URL`: URL to the backend API.
- `MOCK_MODE`: Set to true to use mock data instead of API.
- `APP_ENV`: Application environment (development/production).

## Connecting to backend
Set `BACKEND_BASE_URL` in your `.env` file to point to your backend service.

## Mock mode instructions
Set `MOCK_MODE=true` in `.env` or use the toggle in the app sidebar to run with simulated data.

## Streamlit Cloud deployment steps
1. Push repository to GitHub.
2. Go to share.streamlit.io.
3. Deploy `app.py`.
4. Add environment variables to Streamlit Secrets.

## Verification checklist
- [ ] All pages load without errors
- [ ] Mock data populates correctly
- [ ] CSS loads correctly
- [ ] 3D Scene renders

## Troubleshooting
Check console logs for errors. If 3D scene fails, ensure components/process_canvas.py can access the HTML file.
