<div align="center">
    <h1>VisionAIry</h1>
    <p>Auditory aid for the visually impaired</p>
</div>

These docs are for the code side of Visionairy, physical documentation and CAD files for the case will be updated soon! In-Person Trial Demo Videos: https://drive.google.com/drive/u/2/folders/1_E5NYc_lLohMYZkm3NRx72TlmqosSxUM
## 👋 hello

We use the OpenAI vision API to 
run inference on images, video files, and webcam streams to assist in the visually impaired using our physical device.

🚧 keep in mind that the repository is still under construction

## 💻 Install

```bash
pip install visionairy
```

## 🔑 Keys

You will need an OpenAI API key to use the API. You can get one 
[here](https://platform.openai.com/api-keys).

```bash
export OPENAI_API_KEY=...
```

## 📷 Webcam

```bash
python -m examples.webcam
```
