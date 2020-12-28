# POST Request example

```sh
POST http://127.0.0.1:5000/api/predict

{
    "path" : "C:/Users/alan/PycharmProjects/ParkinsonRecoLib/audio/ok.wav"
}
```

## Deployment

```sh
pip install flask-restful joblib praat-parselmouth pandas numpy sklearn
```

## Start the app

```sh
python api.py
```

## Meta

Alan MARTHINEAU - Karim BENSAID - Augustin LOLLIVIER
