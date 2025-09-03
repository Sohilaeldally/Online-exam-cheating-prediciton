import cv2
import json
from collections import deque, Counter
from inference import InferencePipeline

FRAME_SIZE = (224, 224)
MAX_FPS = 5
VOTING_FRAMES = 5

# Global variables
recent_predictions = deque(maxlen=VOTING_FRAMES)
all_results = []
pipeline = None

def my_sink(result, video_frame):
    """Callback for predictions"""
    global recent_predictions, all_results
    if "predictions" in result and "top" in result["predictions"]:
        label = result["predictions"]["top"]
        recent_predictions.append(label)

        if len(recent_predictions) == VOTING_FRAMES:
            most_common = Counter(recent_predictions).most_common(1)[0][0]
            all_results.append({
                "frame_number": len(all_results) + 1,
                "prediction": most_common
            })
            # Write results to file each time
            with open("predictions.json", "w") as f:
                json.dump(all_results, f, indent=4)


def start_pipeline():
    """Start a new pipeline and reset old results"""
    global pipeline, all_results, recent_predictions
    if pipeline is not None:
        return False

    # Reset previous results
    all_results = []
    recent_predictions = deque(maxlen=VOTING_FRAMES)

    pipeline = InferencePipeline.init_with_workflow(
        api_key="83Cqft9uQa0ZiERn2bSS",
        workspace_name="sohila-reda-82dmq",
        workflow_id="custom-workflow-2",
        video_reference=0,
        max_fps=MAX_FPS,
        on_prediction=my_sink
    )
    pipeline.start()
    return True


def stop_pipeline():
    """Stop the pipeline and return True"""
    global pipeline
    if pipeline is None:
        return False

    pipeline.stop()
    pipeline.join()
    pipeline = None
    return True


def get_results():
    """Return in-memory results"""
    return all_results

