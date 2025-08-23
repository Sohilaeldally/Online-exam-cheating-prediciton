import cv2
import json
from collections import deque, Counter
from inference import InferencePipeline

FRAME_SIZE = (224, 224)
MAX_FPS = 5
VOTING_FRAMES = 5

recent_predictions = deque(maxlen=VOTING_FRAMES)
all_results = []

def my_sink(result, video_frame):
    global recent_predictions, all_results
    if "predictions" in result and "top" in result["predictions"]:
        label = result["predictions"]["top"]
        recent_predictions.append(label)
        if len(recent_predictions) == VOTING_FRAMES:
            most_common = Counter(recent_predictions).most_common(1)[0][0]
            print("Prediction:", most_common)
            all_results.append({
                "frame_number": len(all_results)+1,
                "prediction": most_common
            })
  
            with open("predictions.json", "w") as f:
                json.dump(all_results, f, indent=4)


pipeline = InferencePipeline.init_with_workflow(
    api_key="83Cqft9uQa0ZiERn2bSS",
    workspace_name="sohila-reda-82dmq",
    workflow_id="custom-workflow-2",
    video_reference=0,
    max_fps=MAX_FPS,
    on_prediction=my_sink
)

pipeline.start()
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_resized = cv2.resize(frame, FRAME_SIZE)
        cv2.imshow("Camera", frame_resized)

   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    pipeline.join()
    cap.release()
    cv2.destroyAllWindows()
    print("All results saved in predictions.json")