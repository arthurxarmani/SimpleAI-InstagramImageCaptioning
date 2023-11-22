# SimpleAI-InstagramImageCaptioning
A Python webapp that utilizes an image captioning model with a conversational model.

This is a work-in-progress.

## Usage
```
python main.py

curl -X POST -F 'file=@dog.jpeg' http://127.0.0.1:5000/upload

{
  "caption": "a small dog wearing a red sweater"
}
```