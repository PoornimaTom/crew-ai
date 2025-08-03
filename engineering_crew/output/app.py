```python
import gradio as gr
from audio_surveillance import AudioSurveillance

# Initialize the backend
audio_surveillance = AudioSurveillance()

def analyze_audio(file):
    # Handle upload and file path
    file_path = file.name
    
    # Call the upload method to process the file
    if not audio_surveillance.upload_audio(file_path):
        return "Failed to upload audio file."
    
    # Extract metadata
    metadata = audio_surveillance.extract_metadata(file_path)
    if not metadata:
        return "Failed to extract metadata."
    
    # Visualize the metadata (returning as a JSON string for display)
    metadata_text = '\n'.join([f"{key}: {value}" for key, value in metadata.items()])

    # Generate report
    events = audio_surveillance.search_events([], file_path)
    report_path = audio_surveillance.generate_report(file_path, metadata, events)
    
    return metadata_text, report_path

# Define the Gradio interface
upload_input = gr.inputs.Audio(label="Upload Audio File", type="file")
metadata_output = gr.outputs.Textbox(label="Audio Metadata")
report_output = gr.outputs.Textbox(label="Report Path")

# Set up the interface
interface = gr.Interface(
    fn=analyze_audio,
    inputs=upload_input,
    outputs=[metadata_output, report_output],
    title="Audio Surveillance Analysis",
    description="Upload an audio file to analyze its metadata and generate a report."
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()
```